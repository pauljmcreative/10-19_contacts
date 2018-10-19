from django.shortcuts import render, redirect

# IMPORT DJANGO AUTH
from django.contrib import auth

# Import django user model
from django.contrib.auth.models import User

def register(request):
  if request.method == 'POST':
    # get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check to see if passwords match
    if password == password2:
      # Check if username exists
      if User.objects.filter(username=username).exists():
        return render(request, 'accounts/register.html', {'error': 'That username is already registered.  Please try different username.'})
      else:
        # check for email
        if User.objects.filter(email=email).exists():
          return render(request, 'accounts/register.html', {'error': 'That email has already been registered'})
        else:
          # Register User
          user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
          user.save()
          return redirect('login')
    else:
      return render(request, 'accounts/register.html', {'error': 'Passwords do not match'})
  else:
    return render(request, 'accounts/register.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      return redirect('contacts')
    else:
      return render(request, 'accounts/login.html', {'error': 'Invalid Credentials'})
  else:
    return render(request, 'accounts/login.html')

def logout(request):
  auth.logout(request)
  return redirect('home')