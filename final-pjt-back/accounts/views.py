from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render

from .models import User
from .serializers import modifyUserdata, userSerializer, CustomRegisterSerializer

# Create your views here.
@api_view(['PUT'])
@login_required
def changeUserInfo(request):
    serializer = modifyUserdata(request.user, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
@api_view(['GET'])
# @login_required
def getUserInfo(reqeust, username):
    user = get_user_model().objects.get(username=username)
    serializer = CustomRegisterSerializer(user)
    return Response(serializer.data)