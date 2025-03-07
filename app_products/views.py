from django.shortcuts import render
from django.http import HttpRequest
from .models import AllProductsModel

# Create your views here.
def all_products(request:HttpRequest):
    All_products = AllProductsModel.objects.all()
    for pd in All_products:
        print("---------------------------")
        print(pd.pd_images)
        print("---------------------------")
        print(pd.pd_images.url)
    context = {
        'All_products':All_products
    }
    return render(request, 'app_products/all_products.html', context)