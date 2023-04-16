from django.shortcuts import render
from rest_framework import generics
# from rest_framework import generics, permissions  # new

from .models import Herbs
from .permissions import IsAuthorOrReadOnly  # new
from .serializers import HerbsSerializer
class HerbsList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)  # new
    queryset = Herbs.objects.all()
    serializer_class = HerbsSerializer
    
class HerbsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,) # new
    # permission_classes = (permissions.IsAdminUser,) # new
    queryset = Herbs.objects.all()
    serializer_class = HerbsSerializer

# Create your views here.
