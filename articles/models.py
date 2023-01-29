from django.db import models

# Create your models here.

# 질문 모델
class Question(models.Model):
    question = models.TextField(max_length=100)
    answer1 = models.TextField(max_length=100)
    answer1_letter = models.CharField(max_length=1, blank=True, null=True)
    answer2 = models.TextField(max_length=100)
    answer2_letter = models.CharField(max_length=1, blank=True, null=True)

# mbti 모델 (alphabet컬럼에 선택지? 전부 받아오기)
# hits 필요 없을듯?


# 인물 모델
class Type(models.Model):
    person = models.CharField(max_length=100)
    verse = models.TextField(max_length=100)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    personality = models.TextField(max_length=100, blank=True)
    like = models.TextField(max_length=50, blank=True)
    dislike = models.TextField(max_length=50, blank=True)
    # good_match & bad_match 이미지 링크 넣어서 나중에 불러오기
    good_match = models.CharField(max_length=10, blank=True)
    bad_match = models.CharField(max_length=10, blank=True)
    mbti = models.CharField(max_length=10)