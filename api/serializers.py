from rest_framework import serializers
from api.models import File


class FileRequestSerializer(serializers.Serializer):
    file = serializers.FileField()