from rest_framework import serializers, status, viewsets
from rest_framework.response import Response

from .models import Products
from .serializers import ProductSerailizer

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Products.objects.all()
        serializer = ProductSerailizer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerailizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        product = Products.objects.get(id=pk)
        serializer = ProductSerailizer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = Products.objects.get(id=pk)
        serializer = ProductSerailizer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        product = Products.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
