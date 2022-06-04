from rest_framework.viewsets import ViewSet
from .serializers import ProductCategorySerializer, ProductSerializer
from .models import Product, ProductCategory
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
            return Response(status=200,data=serializer.data)
        return Response(status=400,data=serializer.errors)
        
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(status=200,data=serializer.data)
    
    def get_product(self,request,product_uuid):
        product = Product.objects.get(uuid=product_uuid)
        serializer = ProductSerializer(product)
        return Response(status=200,data=serializer.data)
    
    def update(self,request,product_uuid):
        product = Product.objects.get(uuid=product_uuid)
        serializer = ProductSerializer(data=request.data,instance=product,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200,data=serializer.data)
        return Response(status=400,data=serializer.errors)
    
    def product_detail(self,request,slug):
        product = Product.objects.filter(slug=slug).last()
        serializer = ProductSerializer(product)
        return Response(status=200,data=serializer.data)
    
    def search_products(self,request):
        query = request.query_params.get("search")
        if not query:
            return Response(status=400,data={"error":"Search Keyword is required"})
        queryset = Product.objects.filter(name__icontains=query)
        serializer = ProductSerializer(queryset,many=True)
        return Response(status=200,data=serializer.data)

class ProductCategoryViewSet(ViewSet):
    permission_classes = (IsAuthenticated|ReadOnly)
    serializer_class = ProductCategorySerializer

    def get_queryset(self,request):
        queryset = ProductCategory.objects.all()
        return queryset

    def create(self,request):
        serializer = ProductSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=400,data=serializer.errors)
        serializer.save()
        return Response(status=200,data=serializer.data)

    def update(self,request,category_uuid):
        instance = ProductCategory.objects.filter(uuid=category_uuid).last()
        if not instance:
            return Response(status=400,data={"error":"Product Category Does not exist"})
        serializer = ProductCategorySerializer(data=request.data,instance=instance)
        if not serializer.is_valid():
            return Response(status=400,data=serializer.errors)
        serializer.save()
        return Response(status=200,data=serializer.data)