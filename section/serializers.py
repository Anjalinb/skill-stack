from rest_framework import serializers

from section.models import Module

class ModuleSerializer(serializers.ModelSerializer):

    class Meta:

        model=Module

        fields="__all__"

        read_only_fields=["id","trainer","created_at","updated_at","course","module_no"]