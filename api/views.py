from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

class GetFile(APIView):

    def post(self, request):
        return Response(status=200)
