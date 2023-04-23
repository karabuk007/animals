from django.shortcuts import render

from django.http import HttpResponse
from .models import *
def index(request):
    return render(request, 'main_page.html')
def for_cats(request):
    posts = Cats.objects.all()
    return render(request, 'animals.html', {'posts': posts, 'page_title': 'Котики'})

def for_dogs(request):
    posts = Dogs.objects.all()
    return render(request, 'animals.html', {'posts': posts, 'page_title': 'Пёсики'})

def for_classmates(request):
    posts = Classmates.objects.all()
    return render(request, 'animals.html', {'posts': posts, 'page_title': 'Одноклассники'})