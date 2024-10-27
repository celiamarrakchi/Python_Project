from django.shortcuts import render
from .models import Participant
from django.views.generic import CreateView 
from django.urls import reverse_lazy,reverse
from .forms import participantForm
from django.contrib.auth.views import LoginView,LogoutView

class userCreateView(CreateView):
    model=Participant
    form_class=participantForm
    template_name="users/register.html"
    success_url=reverse_lazy('login')

class LoginCustumView(LoginView):
    template_name="users/login.html"
    def get_success_url(self) :
        return reverse('listviewconf')
    
class LogoutCustumView(LogoutView):
    next_page=reverse_lazy('login')

