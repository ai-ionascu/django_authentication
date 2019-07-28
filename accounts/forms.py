from django import forms

class UserLoginForm(forms.Form):
    """login form"""
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)