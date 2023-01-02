from django import forms
from .models import Blog,contact

class Blogdata(forms.ModelForm):
    class Meta:
        model=Blog
        fields="__all__"

class contactp(forms.ModelForm):
    class Meta:
        model=contact
        fields="__all__"
