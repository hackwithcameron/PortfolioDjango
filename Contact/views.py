from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from decouple import config
import requests


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': config('CAPTCHA_SECRET_KEY'),
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            ''' End reCAPTCHA validation '''

            if result['success']:
                form.save()
                # Get info from form
                firstName = form.cleaned_data['first_Name']
                lastName = form.cleaned_data['last_Name']
                message = form.cleaned_data['message']
                sender = form.cleaned_data['email_Address']
                # Sending email using Sendgrid and build in Django function
                send_mail(
                    # Subject
                    f'{firstName} {lastName}',
                    # Message including contact email in newline
                    f'{message} \n \nContacts Email Address: {sender}',
                    # Send from email
                    'noreply@cameronhackwith.com',
                    # Send to email
                    [config('EMAIL_ADDRESS')], fail_silently=False)
                return redirect('Success/')
    else:
        form = ContactForm()
        site_key = config("CAPTCHA_SITE_KEY")
        context = {
            'form': form,
            'site_key': site_key
        }
        return render(request, 'Contact/contactHome.html', context)


# Contact form success page
def success(request):
    return render(request, 'Contact/success.html')
