from django.shortcuts import render
from .models import Job

def homepage(request): # nick function
    jobs = Job.objects # take job objects to html page
    # send back html file
    return render(request, 'jobs/home.html', {'jobs':jobs})#3rd is dictionary, Left side string
