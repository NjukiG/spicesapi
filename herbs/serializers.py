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