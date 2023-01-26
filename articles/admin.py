from django.contrib import admin
from .models import Mbti, Type, Question
# Register your models here.
admin.site.register(Mbti)
admin.site.register(Type)
admin.site.register(Question)