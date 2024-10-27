from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Conferences,Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import *
from django.shortcuts import get_object_or_404,redirect
from users.models import Reservation

# Create your views here.
#trajalek la liste des conference_id ili amlelhom reservation
def reserveconf(request,conference_id):
    user=request.user
    conference=get_object_or_404(Conferences,id=conference_id)
    if Reservation.objects.filter(participant=user,conference=conference).count()==0 :
        reservation=Reservation.objects.create(participant=user,conference=conference)
        reservation.save()
        conference.capacity-=1
        conference.save()
    return redirect('listviewconf')



#methode 1 avec une fonction
def conferenceList(request):
    list=Conferences.objects.all().order_by()#ajouter le tri sur .all()
    print(list)
    return render(request,'conferences/conferencelist.html',{'conferenceslist':list})
#methode 2 avec une classe
class conferenceListView(LoginRequiredMixin,ListView):
    login_url=reverse_lazy('login')
    model=Conferences
    template_name="/conferences/conferences_list.html" #par defaut ce nom
    #permet d acceder a la liste dans html 
    context_object_name='conferences'
    #ajout de l import de category
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['category']=Category.objects.all()
        user_reservation=Reservation.objects.filter(participant=self.request.user).values_list('conference_id',flat=True)#recuperation des reservations auxquel user aie reservé 
        context['user_reservation']=user_reservation
        return context
    def get_queryset(self):#modifier l affichage
        category_id=self.request.GET.get('category')#name du select
        query=Conferences.objects.order_by('-start_date')
        if category_id:
             query=Conferences.objects.filter(category=category_id)
        return query
class detailsViewConference(DetailView):
    model=Conferences
    template_name='conferences/conference_detail_view.html'
    context_object_name="conf" #utulisé dans conference_detail_view.html
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        conference = self.get_object()
        # Récupérer les réservations associées à cette conférence
        context['reservations'] = Reservation.objects.filter(conference=conference)
        return context

class createViewConference(CreateView):
    model=Conferences
    form_class=conferenceForm   
    #si on ne va pas utuliser le form on utulise field
    #fields=['title','description','start_date','end_date','location','price','capacity','program','category']
    success_url= reverse_lazy('listviewconf')#il faut l ajouter suite ai click sur le bouton submit

class updateViewConference(UpdateView):
    model=Conferences
    fields=['title','description','start_date','end_date','location','price','capacity','program','category']
    success_url= reverse_lazy('listviewconf')#il faut l ajouter suite ai click sur le bouton submit

class deleteViewConference(DeleteView):
    model=Conferences
    success_url= reverse_lazy('listviewconf')

