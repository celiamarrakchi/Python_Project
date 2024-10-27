from .views import *
from django.urls import path

urlpatterns = [
    path('register/',userCreateView.as_view(),name="register"),
    path('login/',LoginCustumView.as_view(),name="login"),
    path('logout/',LogoutCustumView.as_view(),name="logout")  
]
