from rest_framework import serializers
from only_serializers.models import Players


# global level validation
def is_contact_no_valid(value):
	if len(value) != 10:
		raise serializers.ValidationError('Contact number must be 10 digits')

class PlayerSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=255)
	contact_no = serializers.CharField(max_length=10, validators=[is_contact_no_valid,])
	address = serializers.CharField()
	age = serializers.IntegerField()
	category = serializers.CharField(max_length=255, help_text = 'Football Cricket etc')

	# # field level validation 
	# def validate_age(self, value):
	# 	if value < 18:
	# 		raise serializers.ValidationError('Plz Enter valid age..')
	# 	return value




	def create(self, validated_data):
		return Players.objects.create(**validated_data) # This validated data is database supported

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.contact_no = validated_data.get('contact_no', instance.contact_no)
		instance.address = validated_data.get('address', instance.address)
		instance.age = validated_data.get('age', instance.age)
		instance.category = validated_data.get('category', instance.category)
		instance.save()
		return instance