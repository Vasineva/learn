
from django.urls import path
# Импортируем созданное нами представление
from .views import NewsList, NewsDetail


urlpatterns = [
   path('', NewsList.as_view()),
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:id>', NewsDetail.as_view()),
]
