from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your views here.
@api_view(['GET'])
def profile(request, user_id):
    if request.method == 'GET':
        user = get_user_model().objects.get(pk=user_id)
        seriazlier = UserSerializer(user)
        return Response(seriazlier.data, status=status.HTTP_200_OK)