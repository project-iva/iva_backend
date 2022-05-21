import django.contrib.auth.password_validation as validators
from django.core import exceptions
from rest_framework import serializers

from iva_backend.app.models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        validated_attrs = super().validate(attrs)
        if validated_attrs.get('password1') != validated_attrs.get('password2'):
            raise serializers.ValidationError(
                {'password1': 'Password fields didn\'t match.'})

        try:
            # validate the password and catch the exception
            validators.validate_password(password=validated_attrs.get('password1'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'password1': list(e.messages)})

        return validated_attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(email=validated_data['email'])
        user.set_password(validated_data['password1'])
        user.save()
        return user

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']
