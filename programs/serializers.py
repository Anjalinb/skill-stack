from rest_framework import serializers
from programs.models import Course

from section.models import Module
from section.serializers import ModuleSerializer

class CourseSerializer(serializers.ModelSerializer):

    modules=serializers.SerializerMethodField(read_only=True)

    class Meta:

        model=Course

        fields="__all__"

        read_only_fields=["id","trainer","created_at","updated_at"]


    def get_modules(self,obj):

        modules=Module.objects.filter(course=obj)

        serializer_instance=ModuleSerializer(modules,many=True)

        return serializer_instance.data