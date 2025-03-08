from django.shortcuts import render,redirect
from django.db.models import Q
from .models import FriendProfile,Friend
from .forms import FriendProfileSearchForm
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

def search_friends(request):
    friends = FriendProfile.objects.all()  # Start with all profiles

    if request.method == 'GET':
        form = FriendProfileSearchForm(request.GET)
        if form.is_valid():
            search_field = form.cleaned_data['search_field']
            search_value = form.cleaned_data['search_value']
            
            # Use Q objects to create dynamic queries based on selected field
            if search_field == 'year':
                friends = friends.filter(year=search_value)  # Assuming 'year' is an integer
            else:
                friends = friends.filter(**{f"{search_field}__icontains": search_value})

    else:
        form = FriendProfileSearchForm()

    return render(request, 'search/search.html', {
        'form': form,
        'friends': friends
    })

# profiles/views.py
def suggest_friends(request):
    user_profile = FriendProfile.objects.get(user=request.user)
    suggested_friends = FriendProfile.objects.filter(
        hometown=user_profile.hometown, school=user_profile.school
    ).exclude(user=request.user)
    
    return render(request, 'search/suggested_friends.html', {'suggested_friends': suggested_friends})


# create,deleteand update views

class FriendDetail(LoginRequiredMixin,DetailView):
    model=FriendProfile
    template_name='memories/friend_detail.html'
    



class CreateMemory(LoginRequiredMixin,CreateView):
    model=FriendProfile
    fields=['school','secondary_school','University_or_college','interests','country','year']
    template_name='memories/memory_form.html'
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    



class FriendMemoryUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = FriendDetail
    template_name='memories/memory_from.html'
    fields = ['school','secondary_school','University_or_college','interests','country']

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()

        if self.request.user == post.user:
            return True
        else:
            return False
    
    
    
        
class FriendMemoryDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = FriendProfile
    template_name='memories/memory_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.user:
            return True
        else:
            return False
        





@login_required
def add_friend(request, user_id):
    user_to_add = get_user_model().objects.get(id=user_id)

    if user_to_add != request.user:  # Ensure the user is not adding themselves
        # Check if the user is already a friend
        if not Friend.objects.filter(user=request.user, friend=user_to_add).exists():
            # Create friendship (bi-directional)
            Friend.objects.create(user=request.user, friend=user_to_add)
            Friend.objects.create(user=user_to_add, friend=request.user)
            return redirect('friends_list')  # Redirect to the friends list page
    return redirect('error_page')  # Redirect if the user can't be added


@login_required
def friends_list(request):
    friends = Friend.objects.filter(user=request.user)
    return render(request, 'friends/friends_list.html', {'friends': friends})


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# View for Similar Interests
# views.py

from django.shortcuts import render
from django.db.models import Q
from .models import FriendProfile

def get_users_with_similar_interests(request):
    user_profile = FriendProfile.objects.get(user=request.user)

    # Get the user's interests (assumed to be a comma-separated string)
    user_interests = user_profile.interests.split(',')

    # Check if user has any interests at all
    if not user_interests or user_interests == ['']:  # Empty or blank interests
        return render(request, 'search/similar_interests.html', {'error': "You have not specified any interests."})

    # Start with an empty Q object to accumulate the conditions
    query = Q()

    # Dynamically create Q objects for each interest
    for interest in user_interests:
        interest = interest.strip()  # Remove leading/trailing spaces
        if interest:  # Only add to the query if the interest is not empty
            query |= Q(interests__icontains=interest)

    # If no interests were provided (after stripping empty ones), return an error
    if not query:
        return render(request, 'search/similar_interests.html', {'error': "No valid interests provided for search."})

    # Filter friends who have at least one matching interest with the user
    shared_interests = FriendProfile.objects.filter(query).exclude(user=request.user)

    return render(request, 'search/similar_interests.html', {'suggested_friends': shared_interests})


@login_required
def similar_interests(request):
    # Logic to find users with similar interests
    users = get_users_with_similar_interests(request.user)  # Implement this function as per your logic
    return render(request, 'search/similar_interests.html', {'users': users})

# View for About Page
def about(request):
    return render(request, 'search/about.html')


def error_page(request):
    return render(request, 'friends/error.html') 



