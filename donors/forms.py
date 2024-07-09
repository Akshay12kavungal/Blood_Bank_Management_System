

from django import forms
from .models import Donor, Patient
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['name','blood_group', 'phone_number', 'address', 'availability']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name','blood_group_needed', 'phone_number', 'address']



class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']