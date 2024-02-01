import time
from celery import shared_task
from api.models import File
from django.shortcuts import get_object_or_404
import logging


logger = logging.getLogger('main_log')


@shared_task()
def processing_file(file_object_id):
    logger.info('Идёт процесс обработки')
    time.sleep(20)
    logger.info('Процесс завершен')
    file_object = get_object_or_404(File, pk=file_object_id)
    file_object.processed = True
    file_object.save()

