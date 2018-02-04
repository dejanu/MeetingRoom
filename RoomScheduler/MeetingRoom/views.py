from django.shortcuts import render
from rest_framework import generics

from . import serializers
from . import models

# Create your views here.
class RoomList(generics.ListCreateAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer


class RoomDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer