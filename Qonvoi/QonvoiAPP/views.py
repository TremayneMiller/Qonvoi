from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    # response = 'Index Page'
    return render(request, 'qonvoi/index.html')


def topics(request):
    # response = 'This is the Topic View Page'
    return render(request, 'qonvoi/topics.html')


def mentors(request):
    # response = 'This is the Mentor View Page'
    return render(request, 'qonvoi/mentors.html')


def mentees(request):
    # response = 'This is the Mentee View Page'
    return render(request, 'qonvoi/mentees.html')


def user_profile(request):
    # response = 'This is the The User Profile View Page'
    return render(request, 'qonvoi/user_profile.html')


def workspace(request):
    # response = 'This is the Collaboarative worspace View Page'
    return render(request, 'qonvoi/workspace.html')


def dashboard(request):
    # response = 'This is the Dashboard View Page'
    return render(request, 'qonvoi/dashboard.html')
