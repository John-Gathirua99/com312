
from django.shortcuts import render, redirect,HttpResponseRedirect
from .models import Message,Notification,FriendRequest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# def send_message(request, receiver_id):
#     receiver = get_user_model().objects.get(id=receiver_id)
#     if request.method == 'POST':
#         message_text = request.POST['message']
#         Message.objects.create(sender=request.user, receiver=receiver, message_text=message_text)
#         return redirect('inbox')
#     return render(request, 'messaging/send_message.html', {'receiver': receiver})



# def inbox(request):
#     messages = Message.objects.filter(receiver=request.user)
#     return render(request, 'messaging/inbox.html', {'messages': messages})


##Select recipient to send a message

@login_required
def select_recipient(request):
    """View to allow the user to select a recipient to start a conversation with."""
    users = get_user_model().objects.exclude(id=request.user.id)  # Exclude the current user
    return render(request, 'messaging/select_recipient.html', {'users': users})

@login_required
def send_message(request, receiver_id):
    receiver = get_user_model().objects.get(id=receiver_id)

    if request.method == 'POST':
        message_text = request.POST['message']
        Message.objects.create(sender=request.user, receiver=receiver, message_text=message_text)
        return redirect('inbox')

    return render(request, 'messaging/send_message.html', {'receiver': receiver})

@login_required
def inbox(request):
    # Fetch all received messages
    received_messages = Message.objects.filter(receiver=request.user)

    # Fetch all sent messages
    sent_messages = Message.objects.filter(sender=request.user)
    
    # Combine received and sent messages, ordered by timestamp
    all_messages = received_messages.union(sent_messages).order_by('-timestamp')

    return render(request, 'messaging/inbox.html', {'messages': all_messages})




