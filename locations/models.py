from django.db import models
from django.utils import timezone

# Create your models here.

# LocationCode = models.SlugField(max_length=20, db_index=True, null=True)  # Code of the Locations table, where the screen is
# Longitude = models.FloatField(default=51.3968255)
# Latitude = models.FloatField(default=8.0638122)
# StreetName = models.CharField(max_length=50, db_index=True, null=True)
# ZIPCode = models.CharField(max_length=7, db_index=True)
# Town = models.CharField(max_length=50, db_index=True)

# Contacts   Link to Table with contacts per hour


class Locations(models.Model):
    Code = models.CharField(max_length=20)
    Name = models.CharField(max_length=50, blank=True, null=True)
    Street = models.CharField(max_length=50, blank=True, null=True)
    ZIP = models.CharField(max_length=10, blank=True, null=True)
    Town = models.CharField(max_length=50, blank=True, null=True)

    # Ändern von Daten in der Konsole:
    # python3 manage.py shell
    # from screens.models import Screens
    # Locations.objects.all()
    # Locations.objects.create(ScreenCode='AAA', ScreenName='TestScreen AAA', ScreenWidth = 2880, ScreenHeight = 1920, XPitch = 50, YPitch = 50, XRes = 576, YRes = 384, IsMobile=False, LocationCode='ARNSBRGALTMARKT38')


def __str__(self):
        return (self.LocationCode, self.LocationName)