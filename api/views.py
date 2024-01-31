from django.db import transaction
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import FileRequestSerializer
from api.models import File
import os


class GetFile(APIView):

    def post(self, request):
        text = {'file': None}
        serializer = FileRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cleaned_data = serializer.validated_data
        if cleaned_data:
            downloaded_file = File.objects.create(file=cleaned_data['file'])
            _, file_name = os.path.split(downloaded_file.file.name)
            text = {
                'uploaded_at': downloaded_file.uploaded_at,
                'file_name': file_name,
                'file_size(in bytes)': downloaded_file.file.size}
        return Response(text, status=201)
