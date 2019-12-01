from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length = 60)

    def __str__(self):
        return self.neighbourhood_name

    def create_neighbourhood(self):
        self.save()
        
    @classmethod
    def delete_neighbourhood(cls, neighbourhood_name):
        cls.objects.filter(neighbourhood_name=neighbourhood_name).delete()


class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatars/', blank = True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = HTMLField()
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

    def __str__(self):
        return self.name