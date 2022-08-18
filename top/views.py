from django.shortcuts import render
from django.shortcuts import HttpResponse 

# Create your views here.
def learner(request):
    return render(request, 'learner.html')

def teacher(request):
    return render(request, 'teacher.html')

def about(reqeust):
    return render(reqeust, 'about.html')

def home(request):
    return render(request, 'home.html')