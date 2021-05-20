from django.urls import path,include
from . import views

urlpatterns = [
    path('add/',views.add,name="add"),
    path('listing/',views.listing,name="listing"),
    path('add_model/',views.add_model,name="add_model"),
    path('delete_model/<int:id>',views.delete_model,name="delete_model"),
    path('edit/<int:id>',views.edit,name="edit"),
]
