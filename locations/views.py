from django.http import HttpResponse
from django.shortcuts import render
from .forms import LocationForm
from locations.models import Locations




# Create your views here.
def locations_view (request):
    return HttpResponse ("Das ist die Seite LOCATIONS")


def location_create_view (request):
    form = LocationForm(request.POST or None)
    locat = Locations
    if form.is_valid():
        form.save()
    else:
        print ("Form for Location is not valid, ")

    context = {'form': form }

    print("Request GET:", request.GET)
    print("Request POST:", request.POST)
    if request.method == "POST":
        Location_Name= request.POST.get('Name')
        print ("Location Name: ", Location_Name)
        print ("Cleaned Data:", form.cleaned_data)
        locat.objects.create (**form.cleaned_data)


    return render(request, "locations/create_location.html", context)
