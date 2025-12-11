from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token

from rest_framework import serializers
from api.models import *

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medium
        fields = ('id', 'title')

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('id', 'title', 'location', 'start_date', 'end_date', 'description', 'active')

class PieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piece
        fields = ('id', 'title', 'filename', 'date', 'media', 'collections', 'description', 'parent', 'children', 'active', 'use_as_wallpaper')