from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.acercav, name='acercav')
]