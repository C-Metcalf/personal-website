from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .forms import ContactForm

# Create your views here.


def portfolio(request):
    if request.method == 'POST':
        pass

    return render(request, 'Portfolio/index.html')


def projects(request):
    return render(request, 'Portfolio/projects.html')


def resume(request):
    return render(request, 'Portfolio/resume.html')


def contact(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        message = name + "\n" + email + "\n" + phone + "\n" + message

        email_message = EmailMessage(
            subject="New Contact Form",
            body=message,
            from_email=email,
            to=["jarheadfro@gmail.com"]
        )
        """
        send_mail(
            subject="New Contact Form",
            message=message,
            from_email=email,
            recipient_list=["jarheadfro@gmail.com"],
            fail_silently=False,
        )
        """
        email_message.send(fail_silently=False)
    contact_form = ContactForm()
    contact_labels = ["Name", "Email", "Phone", "Message", "reCaptcha"]
    contact_info = zip(contact_labels, contact_form)


    
    # return render(request, 'Portfolio/contact.html', {"contact_info": contact_info})
    return render(request, 'Portfolio/contact.html', {"form": contact_form})


def page_not_found(request, exception):
    return render(request, 'Portfolio/page_not_found.html')


