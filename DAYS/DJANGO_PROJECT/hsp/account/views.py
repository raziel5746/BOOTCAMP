from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from . import factory


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')

    if request.method == 'GET':
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def user_factory(request, num):
    factory.fake_user(num)
    return render(request, 'account/user_factory.html')
