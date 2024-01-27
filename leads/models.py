from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

# Create your models here.

# creating a custom user model that inherits from the Abstractuser


class User(AbstractUser):
    # when a user creates an account, the user becomes the default organizer of that account.
    is_organizer = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Lead(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.IntegerField()
    organization = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE)  # allows leads to beunser a current organization
    agent = models.ForeignKey(
        "Agent", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# the agent table inherits its columns from the user model


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


def post_user_created_signal(sender, instance, created, **kwargs):

    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)
