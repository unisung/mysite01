from django.contrib import admin
from django.urls import path, include
from . import views

app_name ='pybo'

urlpatterns = [
    #http://127.0.0.1:8000/pybo/
    path('', views.home, name='home'),
    #http://127.0.0.1:8000/pybo/2/
    path('<int:question_id>/', views.detail, name='details'),
    #http://127.0.0.1:8000/pybo/answer/create/1/
    path('answer/create/<int:question_id>/',
          views.answer_create, name="answer_create"),
    path('question/create/', views.question_create,
           name="question_create")
]
