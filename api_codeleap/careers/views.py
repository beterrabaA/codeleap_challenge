from careers.models import User
from careers.serializers import UserSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        user_serializer = UserSerializer(users,many=True)
        return Response(user_serializer.data)
    elif request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data,status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PATCH','DELETE'])
def user_change_and_delete(request,pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return  Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PATCH':
        user_serializer = UserSerializer(user,data=request.data,partial=True)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data,status=status.HTTP_200_OK)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response({},status=status.HTTP_204_NO_CONTENT)
