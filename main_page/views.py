from django.shortcuts import render

from django.http import HttpResponse
from .models import *
def index(request):
    posts = MainPage.objects.all()
    return render(request, 'main_page_content.html', {'posts': posts})
def for_cats(request):
    posts = Cats.objects.all()
    context = {
        'posts': posts,
        'page_title': 'Котики'
    }
    return render(request, 'animals.html', context=context)

def for_dogs(request):
    posts = Dogs.objects.all()
    context = {
        'posts': posts,
        'page_title': 'Пёсики'
    }
    return render(request, 'animals.html', context=context)

def for_classmates(request):
    posts = Classmates.objects.all()
    context = {
        'posts': posts,
        'page_title': 'Одноклассники'
    }
    return render(request, 'animals.html', context=context)