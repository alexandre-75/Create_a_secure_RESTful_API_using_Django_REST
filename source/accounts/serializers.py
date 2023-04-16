from .models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class SignupSerializer(serializers.ModelSerializer):

    """
    Serializes User objects for creating new user accounts.
    Attributes:
        email (EmailField): The user's email address.
        password (CharField): The user's password.

    Raises:
        None
    """
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user
