from django import forms
from .models import AdminModel

class AdminForm(forms.ModelForm):
    class Meta:
        model= AdminModel
        fields= ["id","email","password","is_active"]