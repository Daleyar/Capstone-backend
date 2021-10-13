from django.http.response import Http404
from rest_framework import status
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import CustomUser
from .serializers import OwnerSerializer
from django.contrib.auth import get_user_model
CustomUser = get_user_model()


class Owners(APIView):  
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        user = CustomUser.objects.filter(id = id)
        serializer = OwnerSerializer(user, many=True)
        return Response(serializer.data)
