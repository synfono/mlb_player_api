from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import Player
from .serializers import PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
