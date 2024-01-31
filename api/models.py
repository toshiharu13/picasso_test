from django.db import models


class File(models.Model):
    file = models.FileField('Тело файла')
    uploaded_at = models.DateTimeField('когда скачено', auto_now_add=True)
    processed = models.BooleanField('Обработан', default=False)

