from django.shortcuts import render, redirect

# IMPORT DJANGO AUTH
from django.contrib import auth

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