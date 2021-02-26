from django.http import HttpResponse
from django.shortcuts import render
from .forms import postscreen

# Create your views here.
from screens.models import Screens
import cgi
def screens_view (request):
#    Screens.objects.get(pk=pk)
    Display = Screens.objects.all()
    Display = Screens.objects.order_by('ScreenName')
#    Screens.objects.get(pk=pk)
    return render(request, 'screens/index.html', {'Wall': Display})


def screen_info (request):
    Display = Screens.objects.all()
    Display = Screens.objects.order_by('ScreenName')
#    Screens.objects.get(pk = pk)
    return render(request, 'screens/index.html', {'Wall': Display})

def screens_info (request, pk):
    Display = Screens.objects.all()
    Display = Screens.objects.order_by('ScreenName')
    Display = Screens.objects.get(pk = pk)
    return render(request, 'screens/screeninfo.html', {'Wall': Display})



def new_screens (request):
    form = postscreen()
    return render(request, 'screens/base.html', {'form': form})