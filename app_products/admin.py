from django.contrib import admin
from .models import AllProductsModel


class ModelAdmin(admin.ModelAdmin):
    list_display = ('pd_name', 'pd_model', 'pd_brand', 'pd_pricing')
    search_fields = ('pd_name', 'pd_model', 'pd_brand')


# Register your models here.
admin.site.register(AllProductsModel, ModelAdmin)