from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    author = serializers.CharField(max_length=100)
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
