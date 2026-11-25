from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from section.models import Module
from section.serializers import ModuleSerializer

from programs.models import Course
from programs.permissions import IsOwner


class ModuleCreateView(APIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    def post(self,request,pk):

        course_obj=get_object_or_404(Course,id=pk)

        form_data=request.data

        serializer_instance=ModuleSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(trainer=request.user,course=course_obj)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)


class ModuleRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsOwner]

    serializer_class=ModuleSerializer
    queryset=Module.objects.all()

    