from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def homeconex(request):
    return render(request, 'authentications/src/login.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']

        if User.objects.filter(username=username):
            messages.error(request, "cet nom d'utilisateur existe déjà")
            return redirect('enregistrer')
        if User.objects.filter(email=email):
            messages.error(request, "cet Email est déjà utilisé")
            return redirect('enregistrer')
        if not username.isalnum():
            messages.error(request, "le nom doit etre alpha numerique")
            return redirect('enregistrer')

        if password != re_password:
            messages.error(request, " les mot de passe ne correspondent pas")
            return redirect('enregistrer')

        my_user = User.objects.create_user(username, email, password)
        my_user.first_name = firstname
        my_user.last_name = lastname
        my_user.save()
        messages.success(request, 'votre compte a été créé success')

        return redirect('login' )

    return render(request, 'authentications/enregistrer/index.html')


def logIn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('listview')
        else:
            messages.error(request, 'Mauvaise authentification')
            return redirect('login')
    return render(request, 'authentications/src/login.html')


def logOut(request):
    logout(request)
    return redirect('login')


def my_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect()
    else:
        print('bad authentication')

# Create your views here.
