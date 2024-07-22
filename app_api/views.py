from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app_api.models import Product
from app_api.serializers import ProductSerializer


class AllProductView(APIView):
    def get(self, request):
        all_products = Product.all()
        serializer = ProductSerializer(all_products, many=True)
        return Response({'all_products': serializer.data})

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
