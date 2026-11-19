from rest_framework import serializers

from accounts.models import User,TrainerProfile

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=["id","username","password","email","phone","role"]

class TrainerProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=TrainerProfile
        fields="__all__"
        read_only_fields=['id','trainer']