from django.utils import timezone
from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Conferences
from users.models import Reservation
from django.db.models import Count
# Register your models here.
class ReservationInline(admin.TabularInline):
    model=Reservation
    extra=1
    readonly_fields=('reservation_date',)
    can_delete=True
#bel toul
"""
class ReservationInline(admin.StackedInline):
    model=Reservation
    extra=1
    readonly_fields=('reservation_date',)
    can_delete=True
"""
class ParticipentFilter(admin.SimpleListFilter):
    title="participant filter"
    parameter_name="participants"
    def lookups(self, request, model_admin):
        return (
            ('0',('No Participants')),
            ('more',('More Participant'))
        )
    def queryset(self,request,queryset):
        if self.value()=='0':
            return queryset.annotate(participant_count=Count('reservations')).filter(participant_count=0)
        if self.value()=='more':
            return queryset.annotate(participant_count=Count('reservations')).filter(participant_count__gt=0)
        return queryset
    
class ConferenceDataFilter(admin.SimpleListFilter):
    title="date conf filter"
    parameter_name="conference date"
    def lookups(self, request, model_admin):
        return (
            ('Past',('Past Conferences')),
            ('Upcoming',('Upcoming Conferences')),
            ('Today',('Today Conferences'))
        )
    def queryset(self,request,queryset):
        if self.value()=='Past':
            return queryset.filter(end_date__lt=timezone.now().date())
        if self.value()=='Upcoming':
            return queryset.filter(start_date__gt=timezone.now().date())
        if self.value()=='Today':
            return queryset.filter(start_date=timezone.now().date())
        return queryset

class conferenceAdmin(admin.ModelAdmin):
    list_display=('title','location','start_date','end_date','price')
    search_fields=('title',)
    list_per_page=2
    ordering=('start_date','title')
    fieldsets=(
        ('description',{
            'fields':('title','description','category','location','price','capacity')
        }),
        ('horraire',{
            'fields':('start_date','end_date','created_at','updated_at')
         }),
         ('documents',{
             'fields':('program',)
         })
    )
    readonly_fields=('created_at','updated_at')
    inlines=[ReservationInline]
    autocomplete_fields=('category',)
    list_filter=('title',ParticipentFilter,ConferenceDataFilter)
admin.site.register(Conferences,conferenceAdmin)