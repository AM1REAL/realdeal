from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['surname', 'name', 'father_name', 'email', 'phone']


class CordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cords
        fields = ['latitude', 'longitude', 'height']

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['level']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['title', 'image']

class ObjectPSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    cords = CordsSerializer()
    level = LevelSerializer()
    image = ImageSerializer()

    class Meta:
        model = ObjectP
        fields = [
                'pk', 'status', 'beauty_title', 'title', 'other_title',
                'connect', 'user', 'cords', 'level', 'image'
                  ]

class AuthEmailObjectPSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectP
        depth = 1
        fields = '__all__'
