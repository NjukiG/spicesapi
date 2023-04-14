from django.shortcuts import render
from rest_framework import generics

from .models import Herbs
from .serializers import HerbsSerializer
class HerbsList(generics.ListCreateAPIView):
    queryset = Herbs.objects.all()
    serializer_class = HerbsSerializer
    
class HerbsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Herbs.objects.all()
    serializer_class = HerbsSerializer

# Create your views here.
