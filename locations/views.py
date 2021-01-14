from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def locations_view (request):
    return HttpResponse ("Das ist die Seite LOCATIONS")