from djongo import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class Submission(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     unique_id=models.CharField( max_length=10,  unique=True)
#     submission_link=models.TextField()
#     kgp_student=models.BooleanField(default=False)


class CustomUser(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=255)
    
class User(AbstractUser):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255, unique=True)
    password=models.CharField(max_length=255)
    username=models.CharField(max_length=255, unique=True)
    is_kgp=models.BooleanField(default=False)
    custom_id=models.CharField(max_length=20, default="XXXXXXXXXX", unique=True)
    submission_link=models.TextField(default="null")
    
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['first_name', 'last_name','email','password','is_kgp']
    