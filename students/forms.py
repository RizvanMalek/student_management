from django import forms
from .models import StudentsModel

class StudentsForm(forms.ModelForm):
    class Meta:
        model= StudentsModel
        fields= ["id","name","email","password","is_active"]