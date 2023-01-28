from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('question/', views.question, name='question'),
    # path(r'^question/nextpage/$', views.nextPage, name='nextpage'),
    path('nextpage/', views.nextPage, name='nextpage'),
    path('result/', views.result, name='result'),
]
