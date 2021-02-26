from django import forms

from .models import Screens

class postscreen(forms.ModelForm):
    class Meta:
        model = Screens
        fields = ('ScreenCode','ScreenName',)