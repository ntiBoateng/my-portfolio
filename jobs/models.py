from tkinter import CASCADE
from django.db import models
from sqlalchemy import ForeignKey

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to="images/")
    summary = models.CharField(max_length=250)



class Home(models.Model):
    name = models.CharField(max_length=30)
    greetings_1=models.CharField(max_length=15)
    greetings_2=models.CharField(max_length=15)
    picture = models.ImageField(upload_to="picture/")
    updateed = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=60)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to="profile/")
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.career
    
class Profile(models.Model):
    about = models.ForeignKey(About,on_delete=models.CASCADE)
    social_name = models.CharField(max_length=20)
    link = models.URLField(max_length=202)
    
    
class Category(models.Model):
    name=models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural="Skills"
        
    def __Str__(self):
            return f'Portfolio {self.id}'
        

class Skills(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=30)
    
    
class Portfolio(models.Model):
    image = models.ImageField(upload_to="portfolio/")
    link = models.URLField(max_length=200)
    
    def __str__(self):
        return f'Portfolio {self.id}'