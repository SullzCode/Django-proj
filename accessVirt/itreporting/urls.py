# itreporting/urls.py

from django.urls import path
from . import views

app_name = 'itreporting'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # Remove or comment out the following line:
    # views,
]