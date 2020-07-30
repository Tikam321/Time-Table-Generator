from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    monday = models.CharField(blank=True,max_length = 30)
    tuesday = models.CharField(blank=True,max_length=30)
    wednesday = models.CharField(blank=True,max_length=30)
    thursday = models.CharField(blank=True,max_length=30)
    friday = models.CharField(blank=True,max_length=30)



    def __str__(self):
        return f"{self.user.username}"


