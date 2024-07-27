from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
#from django.contrib.auth.decorators import login_required
from django.conf import settings
import os

#@login_required(login_url= 'loginpage')
def home(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        # Handle the uploaded file (e.g., save it to a specific directory)
        save_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
        with open(save_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        # Optionally, save additional information to the database or perform other operations
        return HttpResponse("Your file is Successfully uploaded")
    return render(request, 'home.html') 
def register(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1!= pass2:
            return HttpResponse("Incorrect input")
        else:
            my_user = User.objects.create_user(username=uname, email=email, password=pass1)
            my_user.save()
            return redirect('loginpage')
    return render(request,"index.html")
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        pas = request.POST.get('password')
        user=authenticate(request,username=username,password=pas)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Incorrect Input")
    return render(request, 'log.html')


   
   

# Create your views here.

# Create your views here.
