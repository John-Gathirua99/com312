from django.urls import path
from . import views
from django.contrib.auth import views as authviews
urlpatterns = [
    path('',views.front_page,name='home'),
    path('signup/',views.register,name='signup'),
     path('login/',authviews.LoginView.as_view(template_name='realtime_chat/login.html'), name='login2'),
    path('logout/',authviews.LogoutView.as_view(template_name='realtime_chat/logout.html'), name='signout')
]