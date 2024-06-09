from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
# Create your views here.
def home(request):
    return render(request,'home.html')

def user_register(request):
    if request.method == 'POST':
       form = RegistrationForm(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request,'Account created successfully')
           return redirect('login')

    else:
        form = RegistrationForm()

    return render(request,'register.html',{'form': form, 'type' : 'Register'})

def user_login(request):
    if request.method == 'POST':
      form = AuthenticationForm(request,request.POST)
      if form.is_valid():
           user_name = form.cleaned_data['username']
           user_pass = form.cleaned_data['password']
           user = authenticate(username = user_name,password = user_pass)
           if user is not None:
                messages.success(request,'Logged in successfully')
                login(request,user)
                return redirect('profile')

    else:
        form = AuthenticationForm()
    return render(request,'register.html',{'type': 'Login','form': form})

@login_required
def user_profile(request):
    return render(request,'profile.html')

@login_required
def user_logout(request):
    logout(request)
    messages.warning(request,'Logged out successfully')
    return redirect('home')

@login_required
def user_passwordChange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user,data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password Changed')
            return redirect('login')

    else:
        form = PasswordChangeForm(user=request.user)

    return render(request,'pass_change.html',{'form':form,'type': 'Password change with old password'})


@login_required
def user_passwordChange2(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user,data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password Changed')
            return redirect('login')

    else:
        form = SetPasswordForm(user=request.user)

    return render(request,'pass_change.html',{'form':form,'type': 'Password change without old password'})