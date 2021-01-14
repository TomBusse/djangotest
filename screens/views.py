from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def screens_view (request):
#    return HttpResponse ("Das ist die Seite SCREENS")
    return render(request, 'screens/index.html')

