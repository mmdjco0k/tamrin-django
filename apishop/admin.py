from django.contrib import admin
from .models import RecycleShop , ShopModel
from comment.models import CommentModel
from django.contrib.contenttypes.admin import GenericStackedInline 



class CommentInLine(GenericStackedInline):
    model = CommentModel

@admin.register(ShopModel)
class ArticleClassAdmin(admin.ModelAdmin):
    inlines =[CommentInLine]
    list_display = ("title" , "slug" , "status" ,"product_id")
    actions =["disable_status" , "enable_status"]
    prepopulated_fields = {"slug" : ("title",)}
    def disable_status(self , request , queryset):
        queryset.update(status = False)
    
    def enable_status(self , request , queryset):
        queryset.update(status = True)  

@admin.register(RecycleShop)
class RecycleArticlesAdmin(admin.ModelAdmin):
    actions = ["recover"]
    def get_queryset(self , request):
        return RecycleShop.objects.filter(is_deleted = True)
    
    def recover(self , request,queryset):
        queryset.update(is_deleted = False , deleted_at = None , status = True)
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

