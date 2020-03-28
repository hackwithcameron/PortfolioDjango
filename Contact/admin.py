from django.contrib import admin
from .models import Contact

class ContactForm(Contact):
    admin.site.register(Contact)