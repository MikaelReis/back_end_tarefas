from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'titulo', 'concluida', 'criada_em']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
            }

    def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            return user    