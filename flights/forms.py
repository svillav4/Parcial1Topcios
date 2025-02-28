from django import forms
from .models import Flight

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['name', 'typee', 'price']
        widgets = {
            'typee': forms.Select(choices=Flight.TYPE_CHOICES),
        }
