from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class TestAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        context = {
            'first':'Hello',
            'second':'world'
        }
        return Response(context, status=status.HTTP_200_OK)
    
