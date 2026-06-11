from .models import ImagePost
from .serializers import ImagePostSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def image_posts(request):
    posts = ImagePost.objects.all()
    serialized = ImagePostSerializer(posts, many=True)
    return Response(serialized.data)