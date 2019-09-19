from django.urls import path
from djangoapp import views

urlpatterns = [
    path('', views.funkcjo, name='funkcjo'),
    path('help/', views.help, name ='help'),
    path('index/', views.index, name='index')
]
