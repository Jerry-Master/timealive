from django.urls import path

from . import views

app_name = 'viz'
urlpatterns = [
    path('', views.index, name='index'),
]