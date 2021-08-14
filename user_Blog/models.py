from django.db import models
import datetime
from django.utils import timezone

# User Model to add Users
class User(models.Model):
    name=models.CharField( max_length=50)
    password=models.CharField( max_length=50)
    login_count=models.PositiveIntegerField(default=0)
    last_login=models.DateTimeField( auto_now=False, auto_now_add=False)
    timestamps=models.DateTimeField(  auto_now_add=True)

def login_user(sender, request, User, **kwargs):
    User.userprofile.login_count = User.userprofile.login_count + 1
    User.userprofile.save()
# Post Model to add Posts
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    content=models.TextField()
    author=models.CharField(max_length=13)
    slug=models.CharField(max_length=130)
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.title