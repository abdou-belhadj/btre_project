from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
# Create your views here.

def contact(request):
    if request.method == 'POST':
        localcommercial_id = request.POST['localcommercial_id']
        localcommercial = request.POST['localcommercial']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(localcommercial=localcommercial, localcommercial_id=localcommercial_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this localcommercial')
                return redirect('/localcommercials/'+localcommercial_id)

        contact = Contact(localcommercial=localcommercial, localcommercial_id=localcommercial_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        send_mail(
            'Property List Inquiry',
            'There has been an inquiry for ' + localcommercial +' from ' + name + ' with the phone number ' + phone + '.',
            'abderrahmanbelhadj@gmail.com',
            [realtor_email, 'bthouses96@gmail.com'],
            fail_silently=False
        )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')

        return redirect('/localcommercials/'+localcommercial_id)
