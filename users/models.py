from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class Usermanage(AbstractUser):
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(unique=True)

   

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        return super(Usermanage, self).save(*args, **kwargs)
    

class UserEducation(models.Model):
    user = models.OneToOneField(
        Usermanage, on_delete=models.CASCADE, related_name="education")
    degree = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    passing_year = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username