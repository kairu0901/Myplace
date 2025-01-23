from django.contrib.auth.views import LoginView,LogoutView
from .forms import CustomAuthenticationForm

class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = CustomAuthenticationForm

class CustomLogoutView(LogoutView):
    template_name = 'login.html'
