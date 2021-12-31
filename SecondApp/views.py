from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .form import FormCreation
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        user = FormCreation(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request,"Account Created Successfully")
    else:
        user = FormCreation()
    return render(request,'registration.html',{'user':user})
