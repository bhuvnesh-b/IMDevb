from django import forms
from django.forms import fields
from .models import Review, post



class Reviewform(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment','name','email']
        
