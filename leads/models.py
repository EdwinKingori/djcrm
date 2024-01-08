from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# creating a custom user model that inherits from the Abstractuser


class User(AbstractUser):
    pass


class Lead(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.IntegerField()
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

# the agent tablr inherits its columns from the user model


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
