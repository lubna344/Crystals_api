from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.first_name

class Types(models.Model):
    crystal_type_one = models.CharField(max_length=30, unique=True)
    crystal_type_two = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return self.crystal_type_one