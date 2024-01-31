from django.shortcuts import render
from rest_framework.viewsets import ViewSet 
from rest_framework.views import APIView
from .serializer import ProductsSerializer ,ProductsSerializerCreat ,ProductsSerializerPartialUpdate
from .models import ShopModel
from rest_framework.response import Response 
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import   action
from rest_framework.parsers import MultiPartParser , JSONParser , FormParser
from dj_rest_auth.jwt_auth import JWTCookieAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated , AllowAny
from django.contrib.auth.decorators import permission_required
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from user_model.models import User

class ViewShop(ViewSet):
    def list(self , request):
        Products = ShopModel.objects.all()
        serializer = ProductsSerializer(Products , many = True ,  context={'request': request})
        data = serializer.data
        for i in data :
            image = i.get("image")
            i["image"] = request.build_absolute_uri(image)
        return Response(data)

    
    def retrieve(self , request , slug = None):
        Product = get_object_or_404(ShopModel , slug=slug)
        serializer = ProductsSerializer(Product, context={'request': request})
        data = serializer.data 
        image = data.get("image")
        if image:
            data["image"] = request.build_absolute_uri(image)
        return Response(serializer.data)
    


@permission_classes((IsAuthenticated,))
class ViewChangeProducts(ViewSet):
    # authentication_classes = [JWTCookieAuthentication,]
    parser_classes = (MultiPartParser,)
    @swagger_auto_schema(request_body=ProductsSerializerCreat)
    def create(self, request):
        serializer = ProductsSerializerCreat(data=request.data )
        if serializer.is_valid():
            user = request.user
            serializer.validated_data["author"] = user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(
        operation_summary="Partial update a product",
        manual_parameters=[
            openapi.Parameter(
                name='slug',
                in_=openapi.IN_PATH,
                type=openapi.TYPE_STRING,
                description='Slug of the product for partial update'
            ),
        ],
        request_body=ProductsSerializerPartialUpdate(required=False),
        responses={
            200: ProductsSerializerCreat,
        }
    )
    def partial_update(self, request, slug=None):
        product = get_object_or_404(ShopModel, slug=slug)
        serializer = ProductsSerializerCreat(product, partial=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
            operation_summary="update a product",
            manual_parameters=[
                openapi.Parameter(
                    name='slug',
                    in_=openapi.IN_PATH,
                    type=openapi.TYPE_STRING,
                    description='Slug of the product for update'
                ),
            ],
            request_body=ProductsSerializerCreat,
            responses={
                200: ProductsSerializerCreat,
            }
        )
    def update(self , request, slug = None):
        Product = get_object_or_404(ShopModel , slug=slug)
        serializer = ProductsSerializer(Product , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        else :
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)        

    def destroy(self, request, slug=None):
        product = get_object_or_404(ShopModel , slug =slug)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
