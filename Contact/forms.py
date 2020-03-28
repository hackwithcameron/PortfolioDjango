from django.forms import ModelForm
from.models import Contact
from django import forms


class ContactForm(ModelForm):
    message = forms.CharField(max_length=500, widget=forms.Textarea(
        attrs={
            'placeholder': "Write your message here..."
        }))
    widgets = {
        'firstName': forms.TextInput(attrs={'placeholder': "First Name"})
    }
    class Meta:
        model = Contact
        exclude = ['date', 'id']


