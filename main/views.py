from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def main_view (request):
    #import cgi
    #Display = "Das ist ein Display"
    # return HttpResponse ("Das ist die Seite MAIN")
    return render(request, 'main/main.html')