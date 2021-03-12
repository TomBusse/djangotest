from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import edit_screens_form
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime

# Create your views here.
from screens.models import Screens
import cgi
def screens_view (request):
    Display = Screens.objects.all()
    Display = Screens.objects.order_by('ScreenName')
    return render(request, 'screens/index.html', {'Wall': Display})

def screens_info (request, pk):
    Display = Screens.objects.all()
    Display = Screens.objects.order_by('ScreenName')
    Display = Screens.objects.get(pk= pk)
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
    Display= Screens.objects.get (pk= pk)
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = edit_screens_form(request.POST)
        print("Wir sind in der Post-Methode bei Screen",pk)

        # Check if the form is valid:

        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            #actual_screen.due_back = form.cleaned_data['ScreenName']

            actual_screen.CreatorCode="Tom ist toll"
            print("actual_screen saved as:", actual_screen.ScreenName,"Creator:", actual_screen.CreatorCode)
            #save_screen= Screens(ScreenName='Test', ScreenCode='Test',ScreenWidth= 10, ScreenHeight= 11, XPitch= 12, YPitch= 13, XRes= 14, YRes= 15)
            save_screen = Screens(ScreenName= actual_screen.ScreenName, ScreenCode= actual_screen.ScreenCode, ScreenWidth= actual_screen.ScreenWidth, ScreenHeight= actual_screen.ScreenHeight, XPitch=12,
                                  YPitch=13, XRes=14, YRes=15)
            Display.ScreenName= 'AABBCCDD'
                #actual_screen.ScreenWidth
            Display.save()
            success= actual_screen.save()
            save_screen.save()
            print("Wir sind in der Post-Methode bei Screen. Form is valid", pk, "Success=", success)
            # redirect to a new URL:
            # return HttpResponseRedirect(reverse('screens:screens_view'))
            return redirect('screens:screens_info', pk=actual_screen.pk)
        else:
            print("Wir sind in der Post-Methode bei Screen. Form is valid", pk)

    # If this is a GET (or any other method) create the default form.
    else:
        print("Wir sind in der Get-Methode bei Screen. Form is not valid",pk)
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        #form = edit_screens_form(initial={'renewal_date': proposed_renewal_date})
        form = edit_screens_form(initial={'ScreenName': actual_screen.ScreenName,'ScreenCode': actual_screen.ScreenCode,
                                          'ScreenWidth': actual_screen.ScreenWidth ,'ScreenHeight': actual_screen.ScreenHeight,
                                          'XPitch': actual_screen.XPitch, 'YPitch': actual_screen.YPitch, 'XRes': actual_screen.XRes,
                                          'YRes': actual_screen.YRes, 'IsMobile': actual_screen.IsMobile, 'LocationCode': actual_screen.LocationCode,
                                          'CreatorCode': actual_screen.CreatorCode, 'CreationTime': actual_screen.CreationTime,
                                          'InstallationTeam': actual_screen.InstallationTeam})


    context = {
        'form': form,
        'actual_screen': actual_screen,
    }

    return render(request, 'screens/edit_screens.html', context)




def new_screens (request):
    form = postscreen()
    return render(request, 'screens/main.html', {'form': form})
