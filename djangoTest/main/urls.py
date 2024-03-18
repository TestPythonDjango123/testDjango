from main import views
from django.urls import path

urlpatterns = [
    path('', views.mainPage, name='mainPage'),
    path('post/form/', views.postForm, name='postForm'),
    path('post/form/detail', views.postDetail, name='postDetail')
]