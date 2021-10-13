from datetime import date, timezone
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from order.models import Shop, Menu, Order, Order_food
from order.serializers import MenuSerializer, ShopSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from order.views import shop

@csrf_exempt
def order_list(request):
    if request.method == 'GET':
        order_list = Order.objects.all()
        return render(request, 'delivery/order_list.html',{'order_list' : order_list})

    elif request.method == 'POST':
        order_item = Order.objects.get(pk=int(request.POST['order_id']))
        order_item.deliver_finish-1
        order_item.save()
        return render(request, 'delivery/success.html')