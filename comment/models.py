from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey 

class CommentModel(models.Model):
    username = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    comment_id = models.AutoField(primary_key=True)
    content_type = models.ForeignKey(ContentType , on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    
    
    class Meta:
        indexes = [
            models.Index(fields=["content_type" , "object_id" ])
        ]