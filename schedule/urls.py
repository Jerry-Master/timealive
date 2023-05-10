from django.urls import path

from . import views, compute

app_name = 'schedule'
urlpatterns = [
    path('', views.schedule, name='schedule'),
    path('<int:weeks>/', views.schedule, name='schedule_weeks'),
    path('compute/', compute.main, name='compute')
]