from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView


from programs.models import Course
from programs.serializers import CourseSerializer
from programs.permissions import IsOwner

from accounts.permissions import IsTrainer

class CourseListCreateView(APIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsTrainer]

    def get(self,request):

        qs=Course.objects.filter(trainer=request.user)

        serializer_instance=CourseSerializer(qs,many=True)

        return Response(data=serializer_instance.data)

    def post(self,request):

        form_data=request.data

        serializer_instance=CourseSerializer(data=form_data)

        if serializer_instance.is_valid():

            course_obj=serializer_instance.save(trainer=request.user)

            serializer_instance=CourseSerializer(course_obj)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

class CourseRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsOwner]

    serializer_class=CourseSerializer
    queryset=Course.objects.all()