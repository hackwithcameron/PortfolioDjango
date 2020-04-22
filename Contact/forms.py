from django.forms import ModelForm
from.models import Contact
from django import forms


class ContactForm(ModelForm):
    message = forms.CharField(max_length=500, widget=forms.Textarea(
        attrs={
            'placeholder': "Let me know how I can help you..."
        }))
    first_Name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(attrs={'placeholder': "First Name"}))
    last_Name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(attrs={'placeholder': "Last Name"}))
    email_Address = forms.CharField(max_length=50, label='Email Address', widget=forms.EmailInput(attrs={'placeholder': "Email Address"}))

    class Meta:
        model = Contact
        exclude = ['date', 'id']


