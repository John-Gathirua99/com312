from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model

class FriendProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, default='john mwangi')
    age = models.IntegerField(default=63)
    hometown = models.CharField(default='Makutano', max_length=255)
    school = models.CharField(max_length=255,null=True)
    secondary_school = models.CharField(max_length=255,null=True)
    University_or_college= models.CharField(max_length=255,null=True)
    # college=models.CharField(max_length=255,null=True)

    country=models.CharField(max_length=255,null=True)
    year = models.IntegerField()
    interests = models.TextField()


    def __str__(self):
        return self.user.username


    def get_absolute_url(self):

        return reverse('friend_detail',kwargs={'pk':self.pk})
    

##models for adding new friends

class Friend(models.Model):
    user = models.ForeignKey(get_user_model(), related_name="friends", on_delete=models.CASCADE)
    friend = models.ForeignKey(get_user_model(), related_name="friend_of", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)  # Use this if you want an acceptance step

    def __str__(self):
        return f"{self.user} - {self.friend}"
    
    class Meta:
        unique_together = ('user', 'friend')  # Ensure no duplicate friendships
