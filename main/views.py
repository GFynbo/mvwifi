import urllib
import json

from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

import mvwifi.settings as settings

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():

            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            full_name = form.cleaned_data['full_name']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            if not result['success']:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                return render(request, "contact.html", {"form": form})


            try:
                send_mail(full_name, message, from_email, ['info@mvwifi.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})

def success(request):
    return HttpResponse('Success! Thank you for your message.')

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def plans(request):
    return render(request, 'plans.html')

def eula(request):
    return render(request, 'eula.html')

def aup(request):
    return render(request, 'aup.html')
