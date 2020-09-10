from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import dataform
from .forms import SignUpForm, SignInForm
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
from django.shortcuts import redirect

import pickle
pickle_in = open("./models/heartdisease.pkl","rb")
dataset=pickle.load(pickle_in)


# Create your views here.
def test(request):
    if request.method=='POST':
        form=dataform(request.POST)
        temp1=[]
        if form.is_valid():
            temp_data=[]
            temp_data.append(form.cleaned_data.get('age'))
            temp_data.append(form.cleaned_data.get('resting_Blood_Pressure'))
            temp_data.append(form.cleaned_data.get('cholesterol'))
            temp_data.append(form.cleaned_data.get('max_heart_rate_achieved'))
            temp_data.append(form.cleaned_data.get('exercise_relative_to_rest_Oldpeak'))
            temp1.append(temp_data)
            print(temp1)
            prdi=dataset.predict(temp1)
            if prdi[0]==1:
                return render(request,'base/diseasefound.html')
            else:
                return render(request,'base/found.html')
    form=dataform()
    return render(request,'base/base.html',{'form':form})

def register(request):
    if request.method=="POST":
        print(type(request.POST))
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'base/home1.html')
        else:
            return render(request,'base/register_with_error.html')
    else:
        form=SignUpForm()
    return render(request,'base/register.html',{'form':form})
def home(request):
    return render(request,'base/home1.html')

def signin(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        #users=User.all()
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect('/test')
        else:
            return render(request,'base/signin_with_error.html')
    form=SignInForm()
    return render(request,'base/login.html',{'form':form})
def  view_resume(request):
    return render(request,'base/resume.html')
