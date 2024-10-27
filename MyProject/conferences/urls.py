from .views import *
from django.urls import path

urlpatterns = [
    path('list/',conferenceList,name="listconf"),
    path('listViewConference/',conferenceListView.as_view(),name="listviewconf"),#fonction
    path('details/<int:pk>/',detailsViewConference.as_view(),name="detailconf"),#classe
    path('create/',createViewConference.as_view(),name="conference_create"),
    path('update/<int:pk>/',updateViewConference.as_view(),name="conference_update"),
    path('delete/<int:pk>/',deleteViewConference.as_view(),name="conference_delete"),
    path('reservation/<int:conference_id>',reserveconf,name="reserve")
]
