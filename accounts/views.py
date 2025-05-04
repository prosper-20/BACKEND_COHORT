from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework import status


class CreateUserAPIView(APIView):
    
    def post(self, request):
        new_user = UserRegistrationSerializer(data=request.data)
        new_user.is_valid(raise_exception=True)
        new_user.save()
        return Response({"Success": "Thank you for signing up!"}, status=status.HTTP_201_CREATED)

