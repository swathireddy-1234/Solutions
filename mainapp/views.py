from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):   #main screen
    return render(request, 'registration/dashboard.html', {'section': 'dashboard'})


def register_page(request):
    if request.method =="POST":
        username=request.POST["username"]
        phone_number =request.POST["phonenumber"]
        password =request.POST["password"]
        cnf_password =request.POST["confirm_password"]
        return render(request,'registration/registration.html')
   

