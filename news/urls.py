
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('news/<pk>/' , views.detail, name='detail'),
]