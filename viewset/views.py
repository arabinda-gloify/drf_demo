from django.shortcuts import render
from viewset.models import Author, Blog
from rest_framework.viewsets import ModelViewSet
from viewset.serializers import BlogSerializer


# Create your views here.
class BlogDetailsView(ModelViewSet):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer

