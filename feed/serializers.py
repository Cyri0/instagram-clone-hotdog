from rest_framework.serializers import ModelSerializer
from .models import ImagePost

class ImagePostSerializer(ModelSerializer):
    class Meta:
        model = ImagePost
        fields = '__all__'
