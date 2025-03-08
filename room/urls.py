from django.urls import path
from . import views
urlpatterns =[
    path('rooms/',views.rooms,name='room'),
    path('<slug:slug>/',views.room,name='room')
]