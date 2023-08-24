from django.contrib import admin
from django.urls import path, include
from back.views import ReactView
from back.views import CheckUserView


# URL patterns for your Django app
urlpatterns = [
    # Admin panel URL
    path('admin/', admin.site.urls),
    
    # Default route for ReactView
    path('', ReactView.as_view(), name="xxx"),
    
    path('api/check-user/', CheckUserView.as_view(), name='check-user'),

    path('', include('back.urls')),
]
