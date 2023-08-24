from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import React
from django.contrib.auth.models import User

# Create your views here.

# Define a class-based view for React model
class ReactView(APIView):

    serializer_class = ReactSerializer

    # Handle GET request
    def get(self, request):
        # Fetch all React objects and serialize them
        output = [{"email": output.email, "password": output.password}
                  for output in React.objects.all()]
        return Response(output)

    # Handle POST request
    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# Define a view to check user account
@csrf_exempt
def check_user(request):
    if request.method == 'POST':
        data = request.POST  # or request.data for JSON data
        email = data.get('email')
        password = data.get('password')

        try:
            # Check if user exists with the given email and matching password
            user = React.objects.get(email=email)
            if user.password == password:
                return JsonResponse({'match': True})
        except React.DoesNotExist:
            pass

    return JsonResponse({'match': False})

