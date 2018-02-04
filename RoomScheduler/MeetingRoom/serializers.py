from rest_framework import serializers
from  . import models


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','name','capacity','status','description')
        model = models.Room

