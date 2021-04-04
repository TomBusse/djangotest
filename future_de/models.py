from django.db import models
from django.utils import timezone

class future_de_model(models.Model):
    MainPage_StartFrom = models.DateTimeField(blank=False,db_index=True, null=False)
    MainPage_Headline = models.CharField(max_length=50,blank=False, null=False)
    MainPage_HeaderText = models.TextField(max_length=250, blank=False, null=True)

    MainPage_GreyInfoText = models.TextField(max_length=250, blank=False, null=True)

    MainPage_ParagraphHeader_01 = models.TextField(max_length=50, blank=True, null=True)
    MainPage_ParagraphSubHeader_01 = models.TextField(max_length=200, blank=True, null=True)
    MainPage_ParagraphText_01 = models.TextField(max_length=10000, blank=True, null=True)
    MainPage_ParagraphImage_01 = models.ImageField(upload_to='images', default="Bild01")

    MainPage_ParagraphHeader_02 = models.TextField(max_length=50, blank=True, null=True)
    MainPage_ParagraphSubHeader_02 = models.TextField(max_length=200, blank=True, null=True)
    MainPage_ParagraphText_02 = models.TextField(max_length=10000, blank=True, null=True)
    MainPage_ParagraphImage_02 = models.ImageField(upload_to='images', default="Bild02")

    MainPage_ParagraphHeader_03 = models.TextField(max_length=50, blank=True, null=True)
    MainPage_ParagraphSubHeader_03 = models.TextField(max_length=200, blank=True, null=True)
    MainPage_ParagraphText_03 = models.TextField(max_length=10000, blank=True, null=True)
    MainPage_ParagraphImage_03 = models.ImageField(upload_to='images', default="Bild03")

    MainPage_MainImage = models.ImageField(upload_to='images')





    MainPage_LinkName_01 = models.CharField(max_length=25, blank=True, null=True)
    MainPage_Link_01 = models.URLField(max_length=250, blank=True, null=True)
    MainPage_LinkName_02 = models.CharField(max_length=25, blank=True, null=True)
    MainPage_Link_02 = models.URLField(max_length=250, blank=True, null=True)
    MainPage_LinkName_03 = models.CharField(max_length=25, blank=True, null=True)
    MainPage_Link_03 = models.URLField(max_length=250, blank=True, null=True)
    MainPage_LinkName_04 = models.CharField(max_length=25, blank=True, null=True)
    MainPage_Link_04 = models.URLField(max_length=250, blank=True, null=True)
    MainPage_LinkName_05 = models.CharField(max_length=25, blank=True, null=True)
    MainPage_Link_05 = models.URLField(max_length=250, blank=True, null=True)
    MainPage_LinkName_06 = models.CharField(max_length=25, blank=True, null=True)
    MainPage_Link_06 = models.URLField(max_length=250, blank=True, null=True)
    MainPage_LinkName_07 = models.CharField(max_length=25, blank=True, null=True)
    MainPage_Link_07 = models.URLField(max_length=250, blank=True, null=True)
    MainPage_LinkName_08 = models.CharField(max_length=25, blank=True, null=True)
    MainPage_Link_08 = models.URLField(max_length=250, blank=True, null=True)
    MainPage_LinkName_09 = models.CharField(max_length=25, blank=True, null=True)
    MainPage_Link_09 = models.URLField(max_length=250, blank=True, null=True)

def __str__(self):
        return (self.LocationCode, self.LocationName)