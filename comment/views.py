from .serializer import CommentSerializer
from .models import CommentModel
from apishop.models import ShopModel
from dj_rest_auth.jwt_auth import JWTCookieAuthentication
from django.contrib.contenttypes.models import ContentType
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from user_model.models import User
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class CommentView(APIView):
    authentication_classes = [JWTCookieAuthentication]
    parser_classes = (MultiPartParser,)
    @swagger_auto_schema(
            operation_summary="comment",
            manual_parameters=[
                openapi.Parameter(
                    name='id',
                    in_=openapi.IN_PATH,
                    type=openapi.TYPE_INTEGER,
                    description='id of the product for comment'
                ),
            ],
            request_body=CommentSerializer(),
            responses={
                200: CommentSerializer,
            }
        )
    def post(self , request , pk , format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.validated_data.get("comment")
            content_type= ContentType.objects.get_for_model(ShopModel)
            object_id = pk
            jwt_cookie_auth = JWTCookieAuthentication()
            user = jwt_cookie_auth.authenticate(request)
            if user :
                u = user[1]
                user_id = u.get("user_id")
                username = User.objects.get(id=user_id).username
                CommentModel.objects.create(
                    comment=comment , object_id=object_id ,
                    content_type=content_type , username=username
                )
                return Response({"msg":"your comment has been posted"} ,status=status.HTTP_201_CREATED)
            else :
                return Response({"error":"You are not logged in"} ,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        