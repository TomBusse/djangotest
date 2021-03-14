from django.http import HttpResponse
from django.shortcuts import render
from .forms import LocationForm

# Create your views here.
def locations_view (request):
    return HttpResponse ("Das ist die Seite LOCATIONS")


def location_create_view (request):
    form = LocationForm(request.POST or None)
    validformcode = form.is_valid()
    if form.is_valid():
        form.save()
    else:
        print ("Form for Location is not valid, ",validformcode)

    context = {'form': form }

    return render(request, "locations/create_location.html", context)
