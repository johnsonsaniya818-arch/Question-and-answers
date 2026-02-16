from rest_framework import serializers

from api.models import User

class UserSerializer(serializers.Serializer):

    class Meta:

        model=User

        fields=["id","username","email","password","phone"]

    def create(self, validated_data):
        return User.objects.create(**validated_data)

