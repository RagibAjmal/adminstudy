from django.db.models import fields
from rest_framework import serializers

from .models import Organizer,Events

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = (
            "id",
            "organizer",
            "name",
            "get_absolute_url",
            "mini_description",
            "mini_description",
            "from_date",
            "to_date",
            "get_image",
            "level"
        )