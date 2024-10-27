from django import forms
from .models import Conferences
class conferenceForm(forms.ModelForm):
    class Meta:
        model=Conferences
        fields="__all__"
    start_date=forms.DateField(
        label="conferences start date",
        widget=forms.DateInput(
            attrs={
                'type':'date'
            }
        )
    )
    end_date=forms.DateField(
        label="conferences end date",
        widget=forms.DateInput(
            attrs={
                'type':'date'
            }
        )
    )