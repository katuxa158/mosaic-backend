from PIL import Image
from rest_framework import serializers
from .models import Post

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'image', 'created_at')
        read_only_fields = ('id', 'created_at')

    def validate_image(self, image):
        img = Image.open(image)
        w, h = img.size
        if w != h:
            raise serializers.ValidationError('Image must be square (1:1)')
        return image

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('author', 'likes_count', 'dislikes_count')