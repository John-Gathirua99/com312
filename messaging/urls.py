from django.urls import path
from . import views


urlpatterns=[
    path('inbox/', views.inbox, name='inbox'),
    #  path('conversation/<int:recipient_id>/', views.conversation, name='conversation'),
    path('send_message/<int:receiver_id>/', views.send_message, name='send_message'),
    path('select_recipient/', views.select_recipient, name='select_recipient'),
   
]