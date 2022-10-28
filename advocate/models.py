from email.policy import default
from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="img")
    summary = models.TextField()
    
    def __str__(self):
        return self.name



class Advocate(models.Model):
    username = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=25)
    profile_pic = models.ImageField(upload_to="img")
    bio = models.TextField()
    years_of_experience = models.IntegerField(default=1)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, related_name="advocates")
    
    def __str__(self):
        return self.name


class Link(models.Model):
    advocate = models.OneToOneField(Advocate, on_delete=models.CASCADE, related_name = "links")
    youtube = models.URLField()
    twitter = models.URLField()
    github = models.URLField()
    
    def __str__(self):
        return self.advocate.name

