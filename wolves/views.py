from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def liverpool(request):
    return render(request,"addition.html")

def add(request):
    number1=int(request.POST['num1'])
    number2=int(request.POST['num2'])
    result1=number1+number2
    return render(request,"result.html",{'result':result1})
def sub(request):
    number1=int(request.POST['num1'])
    number2=int(request.POST['num2'])
    result2=number1-number2
    return render(request,"result.html",{'result':result2})
    
    
# views.py
from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm

def create_user(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            # Create a UserProfile object but don't save it yet
            user_profile = form.save(commit=False)
            # You can perform additional processing or validation here
            # Save the object to the database
            user_profile.save()
            return render(request,'result.html')  # Redirect to a success page
    else:
        form = UserProfileForm()

    return render(request, 'create_user.html', {'form': form})