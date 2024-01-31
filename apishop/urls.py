from django.contrib import admin
from django.urls import path , include 
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ViewShop ,ViewChangeProducts 
from rest_framework import routers
from comment.views import CommentView
app_name = "api"
urlpatterns =[
    path('products/', ViewShop.as_view({'get': 'list'}), name = "list"),
    path('products/create/' , ViewChangeProducts.as_view({"post" : "create"}),name="create"),
    path('product/<slug:slug>/' , ViewShop.as_view({"get":"retrieve"}) , name = "detail"),
    path('product/<slug:slug>/change/', ViewChangeProducts.as_view({'put': 'update', 'delete': 'destroy' , "patch":"partial_update"})),
    path("product/<int:pk>/comment/" , CommentView.as_view())
]

