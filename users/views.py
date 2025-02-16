from django.contrib.auth.decorators import login_required
from profile import Profile
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import context
from django.urls import reverse


from users.forms import ProfileForm, UserLoginForm, UserRegisterForm, UserChangeForm



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f'{username}, Ви успішно ввійшли в акаунт')
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
                messages.success(request, f'{user.username}, Ви успішно зарєєстрували акаунт')
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegisterForm()
    
    context = {
        'title':'Home - Реєстрація',
        'form':form
    }
    return render(request, 'users/register.html', context)

@login_required
def profile(request):

    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Профіль успішно змінено')
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title':'Home - Кабінет',
        'form':form
    }
    return render(request, 'users/profile.html', context)

@login_required
def logout(request):
    messages.success(request, f'{request.user.username}, Ви вийшли з акаунта')
    auth.logout(request)
    return redirect(reverse('main:index'))
