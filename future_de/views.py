from django.http import HttpResponse
from future_de.models import future_de_model
from django.shortcuts import render, get_object_or_404, redirect
import cgi
import os



# Create your views here.
def future_de_view (request):
    dirspot = os.getcwd()
    print ("DirSpot:", dirspot)

    SiteInformation = future_de_model.objects.all()
    SiteInformation = future_de_model.objects.order_by('id')[0]

    print ("--",len(SiteInformation.MainPage_HeaderText),"--")
    if (SiteInformation.MainPage_LinkName_09 == "[NULL]"):
        SiteInformation.MainPage_LinkName_09 = "Tom Busse"
    print ("--",SiteInformation.MainPage_LinkName_09,"--")

    #Display = future_de_model.objects.order_by('')
    #return HttpResponse ("Das ist die Seite FUTURE_DE")
    return render(request, 'future_de/future_de.html', {'SiteInfo': SiteInformation})

