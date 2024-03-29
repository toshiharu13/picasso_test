from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import FileRequestSerializer, FileListSerializer
from api.models import File
from api.tasks import processing_file
import os
from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler


log_folder = Path.cwd() / 'logs'
Path(log_folder).mkdir(parents=True, exist_ok=True)
strfmt = '[%(filename)s] [%(asctime)s] [%(levelname)s] > %(message)s'
formatter = logging.Formatter(fmt=strfmt)
logger = logging.getLogger('main_log')
logger.setLevel(logging.INFO)
handler = RotatingFileHandler(Path(log_folder) / 'actions.log', maxBytes=100000, backupCount=5)
handler.setFormatter(formatter)
logger.addHandler(handler)


def decode_file_name(file_string):
    _, file_name = os.path.split(file_string)
    return file_name


class UploadFile(APIView):

    def post(self, request):
        text = {'file': None}
        serializer = FileRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cleaned_data = serializer.validated_data
        if cleaned_data:
            downloaded_file = File.objects.create(file=cleaned_data['file'])
            file_name = decode_file_name(downloaded_file.file.name)
            text = {
                'uploaded_at': downloaded_file.uploaded_at,
                'file_name': file_name,
                'file_size(in bytes)': downloaded_file.file.size
            }
            processing_file.delay(downloaded_file.pk)
        return Response(text, status=201)


class GetListFiles(APIView):
    response_text = {}

    def get(self, request):
        serializer = FileListSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        cleaned_data = serializer.validated_data
        if cleaned_data['show_list']:
            queryset = File.objects.all()
            for file_object in queryset:
                file_name = decode_file_name(file_object.file.name)
                converted_file_object = {
                    'uploaded_at': file_object.uploaded_at,
                    'processed': file_object.processed,
                }
                self.response_text[file_name] = converted_file_object
        return Response(self.response_text, status=200)
