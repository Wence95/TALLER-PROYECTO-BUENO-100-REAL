from django.urls import path

from . import views

urlpatterns = [
    path('', views.eu, name='eu')
]