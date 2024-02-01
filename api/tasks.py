import time
from celery import shared_task
from api.models import File
from django.shortcuts import get_object_or_404


@shared_task()
def processing_file(file_object_id):
    print('Идёт процесс обработки')
    time.sleep(20)
    print('Процесс завершен')
    file_object = get_object_or_404(File, pk=file_object_id)
    file_object.processed = True
    file_object.save()

