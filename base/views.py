from django.shortcuts import render

# Create your views here.
def  view_resume(request):
    return render(request,'base/home.html')
