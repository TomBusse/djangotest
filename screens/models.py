from django.db import models

# Create your models here.
from django.utils import timezone


class Screens(models.Model):
    ScreenCode = models.SlugField(max_length=20, db_index=True)
    ScreenName = models.CharField(max_length=50, db_index=True)
    ScreenWidth = models.IntegerField(null=False)                                   # Display width in mm
    ScreenHeight = models.IntegerField(null=False)                                  # Display height in mm
    XPitch = models.IntegerField(null=False)                                        # Pitch in 1/10mm
    YPitch = models.IntegerField(null=False)                                        # Pitch in 1/10mm
    XRes = models.IntegerField()                                                    # X-Resolution in Pixels
    YRes = models.IntegerField()                                                    # Y-Resolution in Pixels
    IsMobile = models.BooleanField(default=False)                                   # Is the screen mobile or fixed installed?
    LocationCode = models.SlugField(max_length=20, db_index=True, null=True)        # Code of the Locations table, where the screen is
    CreatorCode = models.SlugField(max_length=20, db_index=True, null=True)         # Person who created this entry
    CreationTime = models.DateTimeField(default=timezone.now())                     # Date and time of data entry creation
    InstallationTeam = models.SlugField(max_length=20, db_index=True, null=True)    # Team that built the screen



    # Ändern von Daten in der Konsole:
    # python3 manage.py shell
    # from screens.models import Screens
    # Screens.objects.all()
    # Screens.objects.create(ScreenCode='AAA', ScreenName='TestScreen AAA', ScreenWidth = 2880, ScreenHeight = 1920, XPitch = 50, YPitch = 50, XRes = 576, YRes = 384, IsMobile=False, LocationCode='ARNSBRGALTMARKT38')


def __str__(self):
        return (self.ScreenCode, self.ScreenName)