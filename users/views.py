from django.http import HttpResponse
from django.shortcuts import render
from .forms import EditUsersForm
from users.models import Users


# Create your views here.

def create_user_view (request):
    Uform = EditUsersForm(request.POST or None)
    UData = Users

    if Uform.is_valid():
        Uform.save()
    else:
        print("Form for Location is not valid, ")

    context = {'form': Uform}
    context['Users_Headline'] = "Diese Daten sind zur Benutzung des Portals erforderlich"
#



#    print("Request GET:", request.GET)
#    print("Request POST:", request.POST)
    if request.method == "POST":
        UName = request.POST.get('UserName')
        print("User Name: ",UName)
        print("Cleaned Data:", Uform.cleaned_data)
        UData.objects.create(**Uform.cleaned_data)

    return render(request, "users/users.html", context)

    # return HttpResponse ("Das ist die Seite USERS")
    #return render(request, 'users/users.html')