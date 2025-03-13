from django.db import models

# Create your models here.

class Customers(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


