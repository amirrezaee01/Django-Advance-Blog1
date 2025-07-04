from rest_framework import serializers
from ...models import Post

# class PostSerializer(serializers.Serializer):
#     author = serializers.CharField(max_length=100)
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", 'author', "title", "content", "status",
                  "created_date", "published_date",]
