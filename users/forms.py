from django import forms
from .models import User


class UserForm(forms.ModelForm ):
    bio = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = User
        exclude = ()