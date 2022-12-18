from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from .models import UserCustom
from django.contrib import auth



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('game_list'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'register.html', context)


def profile(request):
    if request.method == 'POST':
        form = UserRegistrationForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'profile.html', context)


def cart(request):
    return render(request, 'cart.html')