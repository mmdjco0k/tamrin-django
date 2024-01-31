from rest_framework import serializers
from rest_framework.serializers import ModelSerializer , HyperlinkedModelSerializer , HyperlinkedRelatedField , HyperlinkedIdentityField
from .models import ShopModel 

class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(
        view_name="apishop:detail" , 
        lookup_field = "slug",
    )
    author = serializers.ReadOnlyField(source="author.username")
    class Meta:
        model = ShopModel
        fields = ("title","detail","url" , "status" , "author",'product_id' , "image")

class ProductsSerializerCreat(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = ShopModel
        fields = ("title", "slug" ,"detail", "status", "product_id", "image")

class ProductsSerializerPartialUpdate(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = ShopModel
        fields = ("title", "detail", "slug", "status", "image")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False