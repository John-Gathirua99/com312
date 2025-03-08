from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
class CustomUser(AbstractUser):
    # Add any additional fields here
    school = models.CharField(max_length=255)
    year = models.IntegerField()

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Custom related name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',  # Custom related name
        blank=True
    
    )

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return str(self.user)
    

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
            super().save(force_insert, force_update, using, update_fields)

