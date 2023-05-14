from django.shortcuts import render
from django.views import generic

class WeatherListView(generic.TemplateView):
    template_name = "weather_report/weather_list.html"