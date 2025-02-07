from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User

# Create your views here.

# --------------------------- USER CRUD OPERATIONS --------------------------

@api_view(['GET'])
def get_users(request):
    return Response(User.objects.all(), status=status.HTTP_200_OK)