from rest_framework import serializers
from ...models import Post


class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
