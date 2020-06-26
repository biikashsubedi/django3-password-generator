from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')

def password(request):

    character = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        character.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('number'):
        character.extend('0123456789')
    if request.GET.get('special'):
        character.extend('!@#$%^&*()')

    length = int(request.GET.get('length'))
    randpassword = ''
    for x in range(length):
        randpassword += random.choice(character)
    return render(request, 'generator/password.html', {'pass': randpassword})

def about(request):
    return render(request, 'generator/about.html')
