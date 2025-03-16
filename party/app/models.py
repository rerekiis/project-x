from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=32)
    wallet = models.IntegerField()
    invited = models.BooleanField(default=False)
    party = models.ForeignKey('Party', on_delete=models.CASCADE)
    

    
class Party(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    people = models.IntegerField()
    date = models.DateField()
    location = models.CharField(max_length=64)
    image = models.ImageField(upload_to='party_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
 
