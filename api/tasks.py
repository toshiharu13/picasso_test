import time
from celery import shared_task
from api.models import File


@shared_task()
def processing_file(file_object):
    print('Идёт процесс обработки')
    time.sleep(20)
    file_object.processed = True
    file_object.save()

