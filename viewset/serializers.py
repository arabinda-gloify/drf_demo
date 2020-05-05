from rest_framework import serializers
from viewset.models import Author, Blog






# Global level validations (This method is outside of the class)

def is_title_valid(value):
	if len(value) <= 10:
		raise serializers.ValidationError('Title must be more than 10 charracters..') 

class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
	title = serializers.CharField(validators=[is_title_valid,])
	class Meta:
		model = Blog
		fields = '__all__'




