from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class WeatherListView(LoginRequiredMixin,generic.TemplateView):
    template_name = "weather_report/weather_list.html"
    login_url = reverse_lazy("login")