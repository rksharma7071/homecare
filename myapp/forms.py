from django import forms
from .models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['FULL_NAME', 'EMAIL', 'PHONE_NUMBER', 'CITY', 'STATE', 'TRADE','IMAGE']
        # label_suffix = ''
        widgets = {
            'FULL_NAME': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'EMAIL': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'PHONE_NUMBER': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'CITY': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city'}),
            'STATE': forms.Select(attrs={'class': 'form-control'}),
            'TRADE': forms.Select(attrs={'class': 'form-control'}),
            'IMAGE': forms.FileInput(attrs={'class': 'form-control'}),
        }
