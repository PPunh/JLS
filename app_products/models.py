from django.db import models

# Create your models here.
class AllProductsModel(models.Model):
    pd_id  = models.AutoField(primary_key=True)
    pd_name = models.CharField(max_length=30)
    pd_model = models.CharField(max_length=30)
    pd_brand = models.CharField(max_length=30)
    pd_description = models.TextField(null=True, blank=True)
    pd_pricing = models.IntegerField()
    pd_images = models.ImageField(upload_to='product_images/', null=True)
    def __str__(self):
        return '{} (id={})'.format(self.pd_name, self.pd_pricing)