from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import User


class UserSerializer(ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=128, write_only=True)

    class Meta:
        model = User
        fields = [
            'user_id',
            'student_id',
            'password_question',
            'password_answer',
            'name',
            'department',
            'password',
            'created_at',
            'updated_at'
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
