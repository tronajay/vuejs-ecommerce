from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import UserSerializer, UserAddressSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Address

class UserAPIViewSet(ViewSet):
    serializer_class = UserSerializer

    def create(self,request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=400,data=serializer.errors)
        serializer.save()
        return Response(status=200,data=serializer.data)
    

class UserAddressViewSet(ViewSet):
    serializer_class = UserAddressSerializer
    permission_classes = (IsAuthenticated,)

    def get_address(self, request):
        queryset = Address.objects.filter(user=request.user)
        serializer = UserAddressSerializer(queryset,many=True)
        return Response(status=200,data=serializer.data)
    
    def create(self,request):
        data = request.data
        data["user"] = request.user.id
        serializer = UserAddressSerializer(data=data)
        if not serializer.is_valid():
            return Response(status=400,data=serializer.errors)
        serializer.save()
        return Response(status=200,data=serializer.data)