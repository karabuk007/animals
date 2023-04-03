from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('dogs/', for_dogs),
    path('cats/', for_cats),
    path('classmates/', for_classmates),
]