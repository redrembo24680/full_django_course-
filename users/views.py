from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import context
from django.urls import reverse

from users.forms import UserLoginForm, UserRegisterForm



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title':'Home - Авторизація',
        'form': form
    }

    return render(request, 'users/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
                form.save()
                user = form.instance
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegisterForm()
    
    context = {
        'title':'Home - Реєстрація',
        'form':form
    }
    return render(request, 'users/register.html', context)

def profile(request):
    context = {
        'title':'Home - Кабінет',
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))
