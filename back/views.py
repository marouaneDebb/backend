from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import React
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate

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




class CheckUserView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = authenticate(username=email, password=password)
        
        if user is not None:
            return Response({'exists': True})
        else:
            return Response({'exists': False})



def register (request):
    if request.method == 'POST' :
        
        password1 = request. POST['password1']
        password2 = request. POST['password2']
        email = request. POST['email']

        user = User.objects.create_user(email='email',password='password1')
        user.save();
        print("user created")