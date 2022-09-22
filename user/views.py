from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import status
from .serializer import userProfile

@api_view(['POST'])
def signup(request):
    pass
