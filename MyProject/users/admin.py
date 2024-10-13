from django.contrib import admin
from .models import Participant,Reservation
from django.db.models import Count
# Register your models here.
class ReservationInline(admin.TabularInline):
    model=Reservation
    extra=1
    readonly_fields=('reservation_date',)
    can_delete=True
#filter les participants par le nombre des reservations faites par eux
class ParticipentFilter(admin.SimpleListFilter):
    title="participant filter by reservation"
    parameter_name="participants"
    def lookups(self, request, model_admin):
        return (
            ('0',('Participants with no reservations')),
            ('more',('Participants with reservations'))
        )
    def queryset(self,request,queryset):
        if self.value()=='0':
            return queryset.annotate(participant_count=Count('reservations')).filter(participant_count=0)
        if self.value()=='more':
            return queryset.annotate(participant_count=Count('reservations')).filter(participant_count__gt=0)
        return queryset
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'participant_category','created_at')
    list_filter = ('participant_category',ParticipentFilter,)
    search_fields = ('username', 'first_name', 'last_name')
    list_per_page= 2
    date_hierarchy='created_at' #affichage selon la date de creation
    readonly_fields=('created_at','updated_at')
    #regroupement
    fieldsets=(
        ('Peronnal information',{
            'fields':('first_name','last_name','email')
        }),
        ('Profil information',{
            'fields':('username','password','participant_category')
         }),
         ('Time',{
             'fields':('created_at','updated_at')
         })
    )
    #rempli la valeur par defaut de l email par username
    prepopulated_fields = {'email': ('username',)}
    #ajouter (model) une reservation au niveau du formualire du participant     
    inlines=[ReservationInline]


    
admin.site.register(Participant,ParticipantAdmin)
admin.site.register(Reservation)