from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length = 60)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    
    @receiver(post_save, sender = User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender = User)

    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_user_profile(self):
        self.save()
