from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Message
from myhostel import settings
from django.core.mail import send_mail
from django.utils.html import strip_tags
from .forms import MessageForm
# Create your views here.

def home(request):
    return render(request, "index.html")

# sign up views.
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username Already Exist")
            return redirect("signup")

        if User.objects.filter(email=email):
            messages.error(request, "Email Already Exist")
            return redirect("signup")

        if len(username)< 4:
            messages.error(request, "Username must be atleast 4 characters")
            return redirect("signup")

        if pass1 != pass2:
            messages.error(request, "Password do not match")
            return redirect("signup")

        if not username.isalnum():
            messages.error(request, "username must be Alph-Numeric")
            return redirect("signup")

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        
        messages.success(request, "Your account has been successfully created")
        return redirect("signin")
        
    return render(request, "signup.html")

# sign in views.
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "home.html", {'fname':fname})

        else:
            messages.error(request, "Invalid Credential")
            return redirect("signin")
    return render(request, "signin.html")

# logout views.
def signout(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect("signin")

def dash(request):
    return render(request, "index.html")

# rendering the complain form.
def complain(request):
    return render(request, "complain.html")

# dashboard views.
@login_required(login_url="signin")
def dashboard(request):
    return render(request, "home.html")

# complain form validation.   
@login_required(login_url="signin")
def send(request):
    form = MessageForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        name = form.cleaned_data.get('name')
        form.save()
        messages.success(request, "Message successfully sent")

        # sending email to corresponding email.
        subject = "Complain Message Received"
        message = "hello" + " " + name + "!! \n" + " We have received your complain \n" + "You will be notified when the problem is solved \n" + " Thank You !!"
        from_email = settings.EMAIL_HOST_USER
        to_list = [email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        return redirect("dash")
    else:
        for field, error in form.errors.items():
            error = strip_tags(error)
            messages.error(request,f"{field}: {error}")
            return redirect("complain")

    