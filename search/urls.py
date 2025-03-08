from django.urls import path

from . import views
from .views import FriendDetail,CreateMemory,FriendMemoryUpdate,FriendMemoryDeleteView
urlpatterns = [
    # path('friends_list/',views.search_friends,name='friends_list'),
    path('search/', views.search_friends, name='search_friends'),
    path('home/details/<int:pk>/',views.FriendDetail.as_view(),name='friend_detail'),
    path('memory/<int:pk>/update/',FriendMemoryUpdate.as_view(),name='memory_update'),
    path('memmory/create/',CreateMemory.as_view(),name='memory_create'),
    path('memory/<int:pk>/delete/',FriendMemoryDeleteView.as_view(),name='memory_delete'),
    ##handling friends
    path('add_friend/<int:user_id>/', views.add_friend, name='add_friend'),
    path('suggested_friends/', views.suggest_friends, name='suggested_friends'),
    path('similar_interests/', views.get_users_with_similar_interests, name='similar_interests'),
    path('about/', views.about, name='about'),
    path('friends/', views.friends_list, name='friends_list'),
     path('error/', views.error_page, name='error_page'),
    
]