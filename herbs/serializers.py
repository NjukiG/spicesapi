from django.contrib.auth import get_user_model  # new
from rest_framework import serializers

from .models import Herbs

class HerbsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "image",
            "body",
            "notes",
            "created_at",
        )
        model = Herbs


class UserSerializer(serializers.ModelSerializer): # new
    class Meta:
        model = get_user_model()
        fields = ("id", "username",)