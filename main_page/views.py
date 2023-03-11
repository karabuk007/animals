from django.shortcuts import render

from django.http import HttpResponse
from .models import *
def index(request):
    return HttpResponse('<h1>Ура, я что-то написал!</h1>')
def for_cats(request):
    posts = Cats.objects.all()
    return render(request, 'cats.html', {'posts': posts, 'page_title': 'Котики'})

def for_dogs(request):
    posts = Dogs.objects.all()
    return render(request, 'dogs.html', {'posts': posts, 'page_title': 'Пёсики'})
