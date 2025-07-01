from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import PostSerializer


@api_view()
def post_list(request):
    return Response({
        'mess age': 'This is a list of posts', })
