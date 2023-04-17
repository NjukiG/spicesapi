from django.contrib.auth import get_user_model  # new
from django.shortcuts import render
from rest_framework import viewsets # new
# from rest_framework import generics
# from rest_framework import generics, permissions  # new
from rest_framework.permissions import IsAdminUser

from .models import Herbs
from .permissions import IsAuthorOrReadOnly  # new
from .serializers import HerbsSerializer, UserSerializer # new


class HerbsViewSet(viewsets.ModelViewSet): # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Herbs.objects.all()
    serializer_class = HerbsSerializer

class UserViewSet(viewsets.ModelViewSet): # new
    permission_classes = [IsAdminUser] # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer



# class HerbsList(generics.ListCreateAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)  # new
#     queryset = Herbs.objects.all()
#     serializer_class = HerbsSerializer
    
# class HerbsDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,) # new
#     # permission_classes = (permissions.IsAdminUser,) # new
#     queryset = Herbs.objects.all()
#     serializer_class = HerbsSerializer

# class UserList(generics.ListCreateAPIView): # new
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
# Create your views here.
