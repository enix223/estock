# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def signin(request):
    # No need to login
    if request.user.is_authenticated():
        render(request, 'home.html')

    if request.method == 'GET':
        return render(request, 'signin.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('index')
        else:
            # invalid login
            return render(request, 'signin.html', {'error': 'Invalid username or password'})


def signout(request):
    logout(request)
    return redirect('signin')


@login_required
def home(request):	
    return render(request, 'home.html')


        

