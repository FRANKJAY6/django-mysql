from .import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles



urlpatterns = [
    path('index/', views.index, name='index'),
    path('html', views.html, name='html'),
    path('demo/', views.demo, name='demo')
]

urlpatterns += staticfiles_urlpatterns()