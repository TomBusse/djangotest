from django.db import models

# Create your models here.
class Screens(models.Model):
    ScreenCode = models.SlugField(max_length=15, db_index=True, unique=True)
    ScreenName = models.CharField(max_length=50, db_index=True, unique=True)
    Longitude = models.FloatField(default=51.3968255)
    Latitude = models.FloatField(default=8.0638122)
    StreetName = models.CharField(max_length=50, db_index=True, null=True)
    ZIPCode = models.CharField(max_length=7, db_index=True)
    Town = models.CharField(max_length=50, db_index=True)
    ScreenWidth = models.IntegerField()                                 # Display width in mm
    ScreenHeight = models.IntegerField()                                # Display height in mm
    XPitch = models.IntegerField()                                      # Pitch in 1/10mm
    YPitch = models.IntegerField()                                      # Pitch in 1/10mm
    XRes = models.IntegerField()                                        # X-Resolution in Pixels
    YRes = models.IntegerField()                                        # Y-Resolution in Pixels

    #Contacts   Link to Table with contacts per hour

    def __str__(self):
        return (self.ScreenCode)