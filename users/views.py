from django.http import HttpResponse
from django.shortcuts import render
from .forms import EditUsersForm
from users.models import Users


# Create your views here.

def create_user_view (request):
    #Uform = EditUsersForm(not (not request.POST and not None))
    Uform = EditUsersForm()
    UData = Users

    if request.method == "POST":
        Uform = EditUsersForm(request.POST)
        UName = request.POST.get('UserName')
        print("User Name: ",UName)

        if Uform.is_valid():
            Uform.save()
            print("Form for Users is valid",Uform.cleaned_data)
        else:
            print(Uform.cleaned_data)
            print("Form for Users is not valid", Uform.errors)
            Uform = Uform (request.POST, instance=Uform)

    context = {'form': Uform}
    context['Users_Headline'] = "Felder mit * müssen ausgefüllt werden."

#    print("Request GET:", request.GET)
#    print("Request POST:", request.POST)
#    if request.method == "POST":
#        UName = request.POST.get('UserName')
#        print("User Name: ",UName)
#        if Uform.is_valid():
#            print("Cleaned Data:", Uform.cleaned_data)
#            UData.objects.create(**Uform.cleaned_data)
#        else:
#            print("Form is not valid:\n", Uform.errors)

    return render(request, "users/users.html", context)

    # return HttpResponse ("Das ist die Seite USERS")
    #return render(request, 'users/users.html')