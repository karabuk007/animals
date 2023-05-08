from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home' ),
    path('dogs/', for_dogs, name='dogs'),
    path('cats/', for_cats, name='cats'),
    path('classmates/', for_classmates, name='classmates'),
]