# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from .forms import RegistrationForm
from django.contrib.auth.views import LoginView

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdate,UpdateForm,Userform
from django.contrib import messages




def register(request):
  
  form = Userform()
  if request.method == 'POST':
    form = Userform(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.info(request,f'{username} has successfully created an account')
      return redirect('login')
  context = {'form':form}
  return  render(request,'users/register.html',context)



@login_required
def profile(request):
    if request.method == "POST":
        update_form = UpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdate(request.POST,request.FILES,instance=request.user.profile)

        if update_form.is_valid() and profile_form.is_valid():
            update_form.save()
            profile_form.save()
            messages.success(request,f'Account successfully updated')
            return redirect('profile')
    else:
        update_form = UpdateForm(instance=request.user)
        profile_form = ProfileUpdate(instance=request.user.profile)
    context = {
        'update_form': update_form,
        'profile_form': profile_form
    }
    return render(request,'users/profile.html',context)

def logoutview(request):
    logout(request)
    return render(request,'users/logout.html')
