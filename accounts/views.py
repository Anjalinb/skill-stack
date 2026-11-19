from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication,permissions

from accounts.models import User,TrainerProfile
from accounts.serializers import UserSerializer,TrainerProfileSerializer
from accounts.permissions import IsTrainer

class UserSignUpView(APIView):

    def post(self,request):

        form_data=request.data
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            user_obj=User.objects.create_user(**cleaned_data)
            serializer_instance=UserSerializer(user_obj)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)


class AdminSignUpView(APIView):

    def post(self,request):

        form_data=request.data
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            admin_obj=User.objects.create_superuser(**cleaned_data)
            serializer_instance=UserSerializer(admin_obj)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class TrainerProfileUpdateView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated,IsTrainer]

    def put(self,request):

        form_data=request.data

        trainer_obj=TrainerProfile.objects.get(trainer=request.user)

        serializer_instance=TrainerProfileSerializer(data=form_data,instance=trainer_obj)

        if serializer_instance.is_valid(): 

            serializer_instance.save()

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

class TrainerProfileDetailView(APIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated,IsTrainer]

    def get(self,request):

        qs=TrainerProfile.objects.get(trainer=request.user)

        serializer_instance=TrainerProfileSerializer(qs)

        return Response(data=serializer_instance.data)


