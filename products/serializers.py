from django.db.models import fields
from rest_framework import serializers

from .models import Category,Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail"
        )