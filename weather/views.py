]from django.shortcuts import render
from django.views import View
import requests
from bs4 import BeautifulSoup


class Main(View):

    # Returns weather data from MetOffice source
    @staticmethod
    def met_office():

        # Initialization -- getting data
        res = requests.get('https://www.metoffice.gov.uk/weather/forecast/gcpkp1hpq#?nearestTo=GU15')
        soup = BeautifulSoup(res.text, 'html.parser')

        # Making raw data workable
        holding_data = str(soup.find_all(class_='off-screen')[4]).split('\n')
        holding_data.pop(0)
        holding_data.pop()
        holding_data = str(holding_data).replace("'", '').replace('[', '').replace(']', '').replace(',', '').split()
        # holding_data = ''.join([i for i in str(holding_data) if "'[]," not in i]).split()

        return {'day_temperature': holding_data[3], 'night_temperature': holding_data[9], 'weather': holding_data[12]}

    @staticmethod
    def post(request):
        pass

    # Returns template response with according data as context
    def get(self, request):
        '''
        context = {
            'met_office': self.met_office(),
        }
        '''
        return render(request, 'weather_main/main.html', {'met_office': self.met_office()})
