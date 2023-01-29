from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('question/', views.question, name='question'),
    path('nextpage/', views.nextPage, name='nextpage'),
    path('result/<mbti>', views.result, name='result'),
]
