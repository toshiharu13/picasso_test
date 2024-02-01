from django.urls import path
from api import views


urlpatterns = [
    path('upload/', views.UploadFile.as_view(), name='upload_file'),
    path('files/', views.GetListFiles.as_view(), name='get_list_files'),
]
