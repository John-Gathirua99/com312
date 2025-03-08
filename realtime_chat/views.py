from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib.auth import login,logout
# Create your views here.


def front_page(request):
    return render(request,'realtime_chat/home.html')



def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request,user)
            return redirect('home')
        
    else:
        form= SignUpForm()
        return render(request, 'realtime_chat/signup.html',{'form':form})
