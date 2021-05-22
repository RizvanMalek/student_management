from django import views
from django.urls import path
from . import views
urlpatterns = [    
    path('add/',views.add,name='add'),
    path('add_model/',views.add_model,name='add_model'),
    path('listing/',views.listing,name='listing'),
]
