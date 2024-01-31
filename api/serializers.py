from rest_framework import serializers
from api.models import File


class FileRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ('file', 'uploaded_at', 'processed')