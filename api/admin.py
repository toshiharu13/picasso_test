from django.contrib import admin
from api import models


@admin.register(models.File)
class FileAdmin(admin.ModelAdmin):
    ...
