from django.db import models

# Create your models here.

class Ask(models.Model):
    question = models.TextField()
    answer1 = models.TextField()
    answer2 = models.TextField()
    alphabet = models.BooleanField(default=False) 


class Mbti(models.Model):
    alphabet = models.CharField()
    hits = models.PositiveIntegerField(default=0)


class Type(models.Model):
    person = models.CharField() 
    verse = models.TextField()
    mbti =  models.CharField()
    
