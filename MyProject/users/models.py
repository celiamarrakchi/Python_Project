from django.db import models
from django.contrib.auth.models import AbstractUser
from conferences.models import Conferences
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db.models.functions import TruncDate
def email_validator(value):
    if not value.endswith('@esprit.tn'):
        raise ValidationError('Email invalide only @esprit.tn are allowed')
# Create your models here.
class Participant(AbstractUser):
    cin_validator=RegexValidator(regex=r'^\d{8}$', message='this field must containt exactly 8 numbers')
    cin=models.CharField(primary_key=True,max_length=8,validators=[cin_validator])
    email=models.EmailField(unique=True,max_length=255,validators=[email_validator])
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    username=models.CharField(unique=True,max_length=255)
    USERNAME_FIELD='username'
    CHOICES=(
        ('etudiant','etudiant'),
         ('enseignant','enseignant'),
        ('doctorant','doctorant'),
        ('chercheur','chercheur' ),

    )
    participant_category=models.CharField(max_length=255,choices= CHOICES)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    reservations=models.ManyToManyField(Conferences,through='Reservation',related_name='reservations')
    class Meta:
         verbose_name_plural="Participant"

class Reservation(models.Model):
    confirmed=models.BooleanField(default=False)
    reservation_date=models.DateTimeField(auto_now_add=True)
    conference=models.ForeignKey(Conferences,on_delete=models.CASCADE)
    participant=models.ForeignKey(Participant,on_delete=models.CASCADE)
    def clean(self):
        if self.conference.start_date<timezone.now().date():
            raise ValidationError("You can only reserve for upcoming conference")
        reservation_count=Reservation.objects.filter(
            participant=self.participant,
            reservation_date__date=timezone.now().date()
        ).count()
        
        print(reservation_count)
        if reservation_count>=2:
             raise ValidationError("You can only make up to three reservations per day")

    class Meta:
        unique_together=('conference','participant')#ajouter la contrainte que un participant peut acceder a une conference et vice versa
    def __str__(self):
        return f"title of reserved conference {self.conference.title}"
        
       