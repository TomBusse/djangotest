from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import edit_screens_form
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime

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

def edit_screens (request):
    form = edit_screens_form()
    Display = Screens.objects.all()
    Display = Screens.objects.order_by('ScreenName')
    #Display = Screens.objects.get(pk = pk)
    #return render(request, 'screens/screeninfo.html', {'Wall': Display})
    return render(request, 'screens/edit_screens.html', {'form': form})
    #return render(request, 'screens/edit_screens.html', {'Wall': Display})

def renew_screens (request, pk):
    actual_screen = get_object_or_404(Screens, pk=pk)
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = edit_screens_form(request.POST)
        print("Wir sind in der Post-Methode bei Screen",pk)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            actual_screen.due_back = form.cleaned_data['ScreenName']
            actual_screen.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('screens:screens_view'))

    # If this is a GET (or any other method) create the default form.
    else:
        print("Wir sind in der Get-Methode bei Screen",pk)
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = edit_screens_form(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'actual_screen': actual_screen,
    }

    return render(request, 'screens/edit_screens.html', context)




def new_screens (request):
    form = postscreen()
    return render(request, 'screens/base.html', {'form': form})