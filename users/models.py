from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member')
    name = models.CharField(max_length=100)
    outstanding_debt = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    national_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
    
    