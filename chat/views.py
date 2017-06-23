from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Chat
from dbmail.models import MailTemplate
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from chat.form import ContactForm
from django.conf import settings
#send_mail('Your Email subject', 'Your Email message.', 'sender_email@example.com', ['recipient_email@example.com'], fail_silently=False)

def SubscriptionView(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
	
	form_message = form.cleaned_data.get('message')
	emailto = form.cleaned_data.get('email_to')
	form_full_name = form.cleaned_data.get('full_name')
	sub = form.cleaned_data.get('subject')
	subject = sub
	from_email = settings.EMAIL_HOST_USER
	to_email =[from_email, emailto]
	contact_message = " %s "%(
            
            form_message)			
	send_mail(subject,
	        contact_message, 
			from_email, 
			to_email, 
			fail_silently=False)
    else:
        form = ContactForm()
    return render(request, 'forn.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


  





def Home(request):
    c = Chat.objects.all()
    return render(request, "home.html", {'home': 'active', 'chat': c})

def Post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        c = Chat(user=request.user, message=msg)
        if msg != '':
            c.save()
        return JsonResponse({ 'msg': msg, 'user': c.user.username })
    else:
        return HttpResponse('Request must be POST.')
	
def admin1(request, template_name='admin.html'):
   
    return render(request, template_name)	
		
def server_list(request, template_name='server_list.html'):
   
    return render(request, template_name)
	
def Messages(request):
    c = Chat.objects.all()
    return render(request, 'messages.html', {'chat': c})