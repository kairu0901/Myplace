from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class HomeView(LoginRequiredMixin,generic.TemplateView):
    template_name = "home/home.html"
    login_url = reverse_lazy("login")