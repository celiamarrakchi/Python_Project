from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Conferences

# Create your views here.

#methode 1 avec une fonction
def conferenceList(request):
    list=Conferences.objects.all().order_by()#ajouter le tri sur .all()
    print(list)
    return render(request,'conferences/conferencelist.html',{'conferenceslist':list})
#methode 2 avec une classe
class conferenceListView(ListView):
    model=Conferences
    template_name="/conferences/conferences_list.html"
    #permet d acceder a la liste dans html 
    context_object_name='conferences'
    def get_queryset(self):
        return Conferences.objects.order_by('-start_date')
    
class detailsViewConference(DetailView):
    model=Conferences
    template_name='conferences/conference_detail_view.html'
    context_object_name="conf" #utulisé dans conference_detail_view.html