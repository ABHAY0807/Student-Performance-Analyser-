from django.shortcuts import render,redirect

# Create your views here.
from .models import Events
def home(request):
    return render(request,'events/home.html')

def upcoming(request):
    e=Events.objects.all()
    return render(request,'events/upcoming.html',{'events':e})