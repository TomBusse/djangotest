
from django import forms
from .models import Locations
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class LocationForm(forms.ModelForm):

    class Meta:
        model = Locations
        fields = ('Code', 'Name', 'Street', 'ZIP', 'Town')
