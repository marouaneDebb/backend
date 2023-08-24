from django.contrib import admin
from django.urls import path
from app.views import ReactView, check_user

# URL patterns for your Django app
urlpatterns = [
    # Admin panel URL
    path('admin/', admin.site.urls),
    
    # Default route for ReactView
    path('', ReactView.as_view(), name="xxx"),
    
    # API endpoint to check user account
    path('api/check-user', check_user, name='check_user'),
]
