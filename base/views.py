from django.shortcuts import render

# Create your views here.

from search.models import FriendProfile
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


class HomeView(ListView):
    model=FriendProfile
    template_name='base/home.html'
    context_object_name='friends'
    ordering=['-year']


