from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
User=get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required = True, validators=[
                                UniqueValidator(queryset = User.objects.all())])
                                
    password = serializers.CharField(write_only= True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username','password','email','first_name','last_name', 'is_restaurant_owner')

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            is_restaurant_owner = validated_data['is_restaurant_owner']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user