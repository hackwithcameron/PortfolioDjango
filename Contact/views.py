from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import Contact
from django.core.mail import send_mail
from decouple import config

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            # Get info from form
            firstName = form.cleaned_data['first_Name']
            lastName = form.cleaned_data['last_Name']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['email_Address']
            # Sending email using Sendgrid and build in Django function
            send_mail(
                # Subject
                '{} {}'.format(firstName, lastName),
                # Message including contact email in newline
                '{} \n \nContacts Email Address: {}'.format(message, sender),
                # Send from email
                'noreply@cameronhackwith.com',
                # Send to email
                [config('EMAIL_ADDRESS')], fail_silently=False)
            return redirect('Success/')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'Contact/contactHome.html', context)

# Contact form success page
def success(request):
    return render(request, 'Contact/success.html')
