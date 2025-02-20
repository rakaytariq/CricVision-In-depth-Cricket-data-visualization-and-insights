from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
import re
from .models import Question
from .forms import QuestionForm, AnswerForm
from django.http import HttpResponseRedirect

# Create your views here.
def handleLogin(request):
    if request.method == 'POST':
        uname = request.POST.get("username")
        pass1 = request.POST.get("pass1")
        myuser = authenticate(username=uname, password=pass1)

        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Success")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("/Login")
    return render(request, 'Login.html')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def player_analysis(request):
    # return render(request, 'player_analysis.html')
    return redirect('http://127.0.0.1:5001/')

def shot_selection(request):
    # return render(request, 'player_analysis.html')
    return redirect('http://127.0.0.1:5000/')

def team_and_player(request):
    return render(request, 'team_and_player.html')

def trend_analysis(request):
    return render(request, 'http://127.0.0.1:5000/dashboard')


def newsandletter(request):
    return render(request, 'http://127.0.0.1:5004/')

def handleSignup(request):
    if request.method == 'POST':
        uname = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("pass1")
        confirmpassword = request.POST.get("pass2")
        
        if password != confirmpassword:
            messages.warning(request, "Passwords do not match!")
            return redirect('/Signup')
        
        if User.objects.filter(username=uname).exists():
            messages.warning(request, "Username already exists!")
            return redirect('/Signup')

        if User.objects.filter(email=email).exists():
            messages.warning(request, "Email already exists!")
            return redirect('/Signup')

        # Validate password for special characters
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            messages.warning(request, "Password should contain at least one special character!")
            return redirect('/Signup')

        myuser = User.objects.create_user(uname, email, password)
        myuser.save()
        messages.success(request, "Signup Successful! Please login.")
        return redirect('/Login')

    return render(request, 'Signup.html')

def handleLogout(request):
    logout(request)
    messages.info(request, "Logout Successful")
    return redirect("/Login")

def forum(request):
    return redirect('http://127.0.0.1:8001/')

