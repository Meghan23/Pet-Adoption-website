# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Pet


class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(max_length=150, label='Name')
    picture = forms.FileField(label='Picture')
    address = forms.CharField(max_length=100, label='Address')
    city = forms.CharField(max_length=50, label='City')
    contact = forms.IntegerField(label='Contact')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'name', 'picture', 'address', 'city', 'contact')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'name', 'picture', 'address', 'city', 'contact')

    def clean_password(self):
        return self.clean_password


class PetForm(forms.ModelForm):

    class Meta:
        model = Pet
        fields = ['photo', 'name', 'breed', 'sex', 'age', 'color', 'needs', 'bonded']
