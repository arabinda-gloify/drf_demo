from django.shortcuts import render
from only_serializers.models import Players
from rest_framework import generics
from only_serializers.serializers import PlayerSerializer
# Create your views here.

class PlayersListView(generics.ListCreateAPIView):
	queryset = Players.objects.all()
	serializer_class = PlayerSerializer

class PlayersRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Players.objects.all()
	serializer_class = PlayerSerializer

