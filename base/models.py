from django.db import models
from django.conf import settings

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile_image = models.ImageField(
        upload_to='profile_images/',
        blank=True,
        null=True
    )

class Post(models.Model):
    title = models.CharField(max_length= 225)
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post/', blank=True, null=True   )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  

    def __str__(self):
        return self.title



    