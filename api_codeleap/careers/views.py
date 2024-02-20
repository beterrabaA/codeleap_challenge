from careers.models import User
from careers.serializers import UserSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)