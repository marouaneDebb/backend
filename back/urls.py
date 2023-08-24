from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns if you have any
    path('register/', views.register, name='register'),
]
