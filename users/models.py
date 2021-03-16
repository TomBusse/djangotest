from django.db import models

#https://github.com/stefanfoulis/django-phonenumber-field/tree/main/phonenumber_field
#from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
from django.utils import timezone

MESSENGER_CHOICES = [
    ('Telegram', 'TELEGRAM'),
    ('WhatsApp', 'WHATSAPP'),
    ('FaceBook', 'FACEBOOK'),
    ('Threma', 'THREMA'),
    ('SMS', 'SMS'),
]


class Users(models.Model):
    UserName = models.SlugField(max_length=50, db_index=True, null=False, unique=True)
    GivenName = models.CharField(max_length=50, db_index=False, null=False)
    MiddleName = models.CharField(max_length=30, db_index=False, null=True)
    SurName = models.CharField(max_length=50, db_index=True, null=False)
    Street = models.CharField(max_length=50, db_index=True, null=False)
    ZIP = models.CharField(max_length=50, db_index=True, null=False)
    Town = models.CharField(max_length=50, db_index=True, null=False)
    State = models.CharField(max_length=50, db_index=True, null=False)
    EMail = models.EmailField(max_length=70, db_index=False, null=False)
    Phone = models.CharField(max_length=30, null=False, blank=False, unique=True)
    CellPhone = models.CharField(max_length=30, null=False, blank=False, unique=True)
    MessengerType = models.CharField(max_length=10, choices=MESSENGER_CHOICES, null=True, default="Telegram")
    MessengerID = models.CharField(max_length=30, blank=False, unique=True)
    CompanyCode = models.CharField(max_length=20, db_index=True, null=True)
    LocationCode = models.CharField(max_length=22, db_index=False, null=True)
    UserIsVisible = models.BooleanField(default=True)
    CreationTime = models.DateTimeField(default=timezone.now())                     # Date and time of data entry creation




    # Ändern von Daten in der Konsole:
    # python3 manage.py shell
    # from screens.models import Screens
    # Screens.objects.all()
    # Screens.objects.create(ScreenCode='AAA', ScreenName='TestScreen AAA', ScreenWidth = 2880, ScreenHeight = 1920, XPitch = 50, YPitch = 50, XRes = 576, YRes = 384, IsMobile=False, LocationCode='ARNSBRGALTMARKT38')


def __str__(self):
        return (self.ScreenCode, self.ScreenName)