from django.db import models

# Create your models here.

# 질문 모델
class Ask(models.Model):
    question = models.TextField(max_length=100)
    answer1 = models.TextField(max_length=100)
    answer2 = models.TextField(max_length=100)
    alphabet = models.BooleanField(default=False) 

# mbti 모델 (alphabet컬럼에 선택지? 전부 받아오기)
# hits 필요 없을듯?
class Mbti(models.Model):
    alphabet = models.CharField(max_length=100)
    hits = models.PositiveIntegerField(default=0)

# 인물 모델
class Type(models.Model):
    person = models.CharField(max_length=100) 
    verse = models.TextField(max_length=100)
    mbti =  models.CharField(max_length=100)
    
    
    
    
