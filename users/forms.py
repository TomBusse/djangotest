from django import forms
from .models import Users
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class EditUsersForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ('UserName', 'GivenName', 'MiddleName', 'SurName', 'Street', 'ZIP', 'Town', 'State',
                  'EMail', 'Phone', 'CellPhone', 'MessengerType', 'MessengerID', 'CompanyCode',
                  'LocationCode', 'UserIsVisible', 'CreationTime')
