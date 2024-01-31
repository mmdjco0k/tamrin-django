from django.db import models
from django.db.models import Q , Manager,QuerySet
from django.utils import timezone
from user_model.models import User

class SoftQuery(QuerySet):
    def delete(self):
        self.update(is_deleted = True , deleted_at = timezone.now() , status = False)

class SoftManager(Manager):
    def get_queryset(self):
        return SoftQuery(self.model , self._db).filter(Q(is_deleted = False) | Q(is_deleted__isnull = True))


class SoftDelete(models.Model):
    is_deleted = models.BooleanField(default=False , null=True)
    deleted_at = models.TimeField(null=True , blank=True)
    status = models.BooleanField(default=False)
    
    objects = SoftManager()
    
    class Meta:
        abstract = True
    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.status = False
        self.save() 

class ShopModel(SoftDelete):
    product = models.CharField(max_length=250 , blank=False)
    title = models.CharField(max_length=250)
    detail = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250 , unique=True)
    product_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    def __str__(self) :
        return self.title

class RecycleManager(Manager):
    def get_queryset(self):
        return self._queryset_class(self.model , self._db).filter(Q(is_deleted = True) | Q(is_deleted__isnull = False))

class RecycleShop(ShopModel):
    objects = RecycleManager()
    class Meta :
        proxy = True