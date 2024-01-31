from django.urls import path
from api import views


urlpatterns = [
    path('', views.GetFile.as_view(), name='get_file')
]