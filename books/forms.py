from django import forms
from .models import BooksModel

class BooksForm(forms.ModelForm):
    class Meta:
        model= BooksModel
        fields= ["id","name","author","price","img"]