from rest_framework.viewsets import ViewSet
from .serializers import ProductSerializer
from .models import Product
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import ReadOnly

# Create your views here.
class ProductViewSet(ViewSet):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated|ReadOnly,)

    def create(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200,data="Product Created Successfully")
        return Response(status=400,data=serializer.errors)
        
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(status=200,data=serializer.data)
    
    def get_product(self,request,pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(status=200,data=serializer.data)
    
    def update(self,request,pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(data=request.data,instance=product,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200,data="Product Updated Successfully")
        return Response(status=400,data=serializer.errors)