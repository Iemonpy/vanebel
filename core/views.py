from django.views.generic import TemplateView
from django.views import View
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse

from django.core.mail import EmailMultiAlternatives

class HomeView(View):
    def get(self,request,*args, **kwargs):
        
        
        return render(request, 'home.html')

    def post(self,request,*args, **kwargs):
        if request.method == 'POST':
            name  = request.POST['name']
            body  = request.POST['body']
            email  = request.POST['email']
            subject = request.POST['subject']




            template = render_to_string('correo.html', {
                'name': name,
                'body': body,
                'email': email,
                'subject':subject
            })

            email = EmailMultiAlternatives(
                body,
                template,
                settings.EMAIL_HOST_USER,
                ['vanebel.arg@gmail.com']
            )

            email.attach_alternative(template, "text/html")
            email.fail_silently = False
            email.send()

            messages.success(request,'Se ha enviado tu correo')
            return redirect('home')