from django.contrib import admin
from django.urls import path
from . import views

app_name = 'weather_report'
urlpatterns = [
    path('kairu_weather/',views.WeatherListView.as_view(),name='weather_list'),
]