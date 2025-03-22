from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth import login, logout, authenticate


def userSettings(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', request.user.profile)

    context = {'form': form }
    return render(request, 'users/settings.html', context)


def profile(request, username):
    profile = Profile.objects.get(username=username)
    context = {'profile': profile}
    return render(request, 'users/profile.html', context)


def registerUser(request):

    if request.user.is_authenticated:
        return redirect('recipes')

    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            return redirect('recipes')


    context = {'form': form}
    return render(request, 'users/register.html', context)


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
