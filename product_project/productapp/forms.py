from django import forms
from .models import product

class MovieForms(forms.ModelForm):
    class Meta:
        model=product
        fields=['name','desc','year','img']