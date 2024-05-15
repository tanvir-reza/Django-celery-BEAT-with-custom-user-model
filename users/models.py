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
    

class UserLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    update_by = models.ForeignKey(Usermanage, on_delete=models.SET_NULL,null=True)

    class Meta:
        abstract = True


    def __str__(self):
        return self.user.username
    

class UserEducation(UserLog):
    user = models.OneToOneField(
        Usermanage, on_delete=models.CASCADE, related_name="education")
    degree = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    passing_year = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username
    

class PrintShop(models.Model):
    name = models.CharField(max_length=100,default="ABC Publisher",null=False,blank=False)
    address = models.CharField(max_length=100,default="Dhaka",null=False,blank=False)

    def __str__(self):
        return self.name
    

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Usermanage, on_delete=models.CASCADE, related_name="books")
    print_by = models.ManyToManyField(PrintShop,related_name="publishers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def created_at_formatted(self):
        return self.created_at.strftime("%Y-%m-%d %H:%M:%S")
    
    @property
    def updated_at_formatted(self):
        return self.updated_at.strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return self.title + " - " + self.author.username

    
# class Address(models.Model):
#     user = models.OneToOneField(
#         Usermanage, on_delete=models.CASCADE, related_name="address")
#     address = models.CharField(max_length=100)
#     city = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     country = models.CharField(max_length=50)
#     pincode = models.CharField(max_length=10)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.user.username