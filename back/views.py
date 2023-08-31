from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ReactSerializer
from .models import React
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from .models import UploadedFile
from .serializer1 import UploadedFileSerializer


# Create your views here.

# Define a class-based view for React model
class ReactView(APIView):

    serializer_class = ReactSerializer

    # Handle GET request
    def get(self, request):
        output = [{"email": output.email, "password": output.password}
                  for output in React.objects.all()]
        return Response(output)

    # Handle POST request
    def post(self, request):
        email = request.data.get('email')
        
        try:
            existing_user = React.objects.get(email=email)
            return Response({'exists': True})
        except React.DoesNotExist:
            serializer = ReactSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

        return Response({'exists': False})

# Define a view to check user account




class CheckUserView(APIView):
    
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
       
        
        try:
            user = React.objects.get(email=email, password=password)
            return Response({'exists': True})
        except React.DoesNotExist:
            return Response({'exists': False})



class UploadFileView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        serializer = UploadedFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, *args, **kwargs):
        files = UploadedFile.objects.all()
        serializer = UploadedFileSerializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
