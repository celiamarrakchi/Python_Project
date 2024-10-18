from .views import *
from django.urls import path

urlpatterns = [
    path('list/',conferenceList,name="listconf"),
    path('listViewConference/',conferenceListView.as_view(),name="listviewconf"),#fonction
    path('details/<int:pk>/',detailsViewConference.as_view(),name="detailconf")#classe
]
