from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render_to_response, render
from django.core.context_processors import csrf
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.core.urlresolvers import reverse
import random
import string
from healthcare.forms import *

# user login
def user_login(request):
    if request.user.is_anonymous():

        if request.method == 'POST':
            form = UserLoginForm(request.POST)

            if form.is_valid():

                cleaned_data = form.cleaned_data

                user = cleaned_data.get("user")

                login(request, user)
                if user.is_active:
                    login(request, user)
                else:
                    return render_to_response('healthcare/templates/user-login.html',
                                              context)

                if 'next' in request.POST:
                    next_url = request.POST.get('next')
                    return HttpResponseRedirect(next_url)
                return HttpResponseRedirect('/')
        else:
            form = UserLoginForm()

        next_url = request.GET.get('next')

        context = {
            'form': form,
            'next': next_url,
            # 'password_reset': True if next_url else False
        }

        context.update(csrf(request))
        return render_to_response('healthcare/templates/user-login.html', context)
    else:
        return HttpResponseRedirect('/')


@login_required
def user_logout(request):
    context = RequestContext(request)
    logout(request)
    return HttpResponseRedirect('/')

# to register new user and send confirmation link to registerd email id
def account_register(request):
    context = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():

            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            user = User.objects.create_user(username, email, password)
            user.is_active = True
            user.save()
            


            return render(request, 'healthcare/templates/message.html')
        context = {'form': form}
        return render_to_response('healthcare/templates/user-register.html',
                                  context,
                                  context_instance=RequestContext(request))
    else:
        form = RegisterForm()
        context = {
            'form': form
        }
        context.update(csrf(request))
        return render_to_response('healthcare/templates/user-register.html',
                                  context)