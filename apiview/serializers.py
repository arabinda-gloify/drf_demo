from rest_framework import serializers
from apiview.models import Mobile

class MobileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Mobile
		fields = '__all__'
