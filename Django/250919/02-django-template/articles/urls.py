from django.urls import path
# 명시적 상대 경로
from . import views

app_name = 'articles'
urlpatterns = [
    # 클라이언트로 부터 http://127.0.0.1:8000/articles/ 요청이 들어오면
    # articles 앱의 views 모듈의 index 함수가 호출된다.
    path('', views.index, name='index'),
    path('dinner/', views.dinner, name='dinner'),
    path('search/', views.search, name='search'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('<int:num>/', views.detail),
    path('<str:name>/', views.greeting),
]
