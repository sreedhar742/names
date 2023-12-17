# forms.py
from django import forms

class UserProfileForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    # Add more fields as needed
