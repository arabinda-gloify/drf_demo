from django.shortcuts import render
from rest_framework import generics
from apiview.models import Mobile
from apiview.serializers import MobileSerializer


# Create your views here.
class MobileListCreateView(generics.ListCreateAPIView):
	queryset = Mobile.objects.all()
	serializer_class = MobileSerializer

class MobileRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Mobile.objects.all()
	serializer_class = MobileSerializer
