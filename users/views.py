from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def loginUser(request):

    if request.user.is_authenticated:
        return redirect('recipes')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('recipes')
        else:
            print("Username OR password is incorrect")

    return render(request, 'users/login.html')


def logoutUser(request):
    logout(request)
    return redirect('recipes')


def profile(request, username):
    profile = Profile.objects.get(username=username)
    context = {'profile': profile}
    return render(request, 'users/profile.html', context)
