from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView
from product.models import Product
from product.serializers import *


class ProductView(ListView):
    model = Product
    template_name = "product.html"


# view for REST API
@csrf_exempt
def product_list_api(request):
    if request.method == 'GET':
        product = Product.objects.all()
        s = ProductSerializer(product, many=True)
        return JsonResponse({
            "products": s.data
        })
    elif request.method == 'POST':
        s = ProductSerializer(data=request.POST)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data)
        else:
            return JsonResponse(s.errors, status=400)
