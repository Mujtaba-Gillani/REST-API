from rest_framework import serializers
from .models import *

# class PostSerializer(serializers.Serializer):
#     id= serializers.IntegerField(read_only=True)
#     title=serializers.CharField(max_length=256)
#     content=serializers.CharField()
#     created=serializers.DateTimeField(read_only=True)




class PostSerializer(serializers.ModelSerializer):
    title=serializers.CharField(max_length=100)
    class Meta:
        model=Post
        fields=["id","title","content","created"]