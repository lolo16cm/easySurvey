# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    ROLE_CHOICES = [
        ('creator', 'Creator'),
        ('taker', 'Taker'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    

    def __str__(self):
        return f"{self.user.username} - {self.role}"
