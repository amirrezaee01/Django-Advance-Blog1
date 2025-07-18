from rest_framework import serializers

from accounts.models import Profile

from ...models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_url", read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name="get_abs_url")

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "image",
            "title",
            "content",
            "status",
            "category",
            "snippet",
            "relative_url",
            "absolute_url",
            "created_date",
            "published_date",
        ]
        read_only_fields = ["author"]

    def get_abs_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    # Override the to_representation method to customize the output
    # of the serializer if needed.seperate the two part
    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("snippet", None)
            rep.pop("relative_url", None)
            rep.pop("absolute_url", None)
        else:
            rep.pop("content", None)

        rep["category"] = CategorySerializer(instance.category).data
        return rep

    def create(self, validated_data):
        validated_data["author"] = Profile.objects.get(
            user__id=self.context.get("request").user.id
        )
        return super().create(validated_data)
