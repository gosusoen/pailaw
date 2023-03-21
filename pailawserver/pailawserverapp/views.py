from rest_framework import generics
from pailawserverapp.models import Product
from pailawserverapp.serializers import ProductSerializer

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer