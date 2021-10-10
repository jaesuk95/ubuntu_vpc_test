from datetime import date, timezone
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from order.models import Shop, Menu, Order, Order_food
from order.serializers import MenuSerializer, ShopSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt
# csrf 는 보안용, front 와 backend 소통을 할때 중간에 바꿔주는 경우가 있기 때문에 보안하기 위해서 보안적인 요소
def shop(request):
    if request.method == 'GET':
        # 만약 request method 가 get 이라면 

#       밑에 코딩은 insomnia 로 데이터 확인용이다
#        shop = Shop.objects.all()        # Shop 이라는 데이터 베이스를 만든다 
        # Shop 데이터 베이스는 모든 object 을 다 shop 에다가 저장한다. 
 #       serializer = ShopSerializer(shop, many=True) # many = true 라는 뜻은, menu 가 많아도 상관 안하겠다. 
        # 그리고 그 데이터들은 serializer 통해서 JSON 형태 passing 을 해서 JSON 형태로 변환해서,
        # Serializer 라는 것은, 데이터 베이스가 현재 JSON 형태가 아니기 때문에 그것을 편리하게 보여주기 위해 JSON 형태로 바꿔주는 Seriallizer 를 사용한다 
 #       return JsonResponse(serializer.data, safe=False)
        # JSON 형태로 보여 주겠다. 

        shop = Shop.objects.all()
        return render(request, 'order/shop_list.html', {'Shop_list':shop})
        # Shop.object.all 에 있는 모든 object 들이 Shop_list 라는 이름으로 html 으로 향해 들어간다 


    elif request.method == 'POST':
        # 데이터를 추가하는 목적 

        data = JSONParser().parse(request)
        # 데이터에서 JSONParser (JSONParser is the base class to define public API for reading JSON content. It is the most efficient way for reading JSON data.)
        # 어떤 데이터를 추가 할 것인지 JSON 형태 나와있기 때문에 그것을 Parsing 한 다음에 

        serializer = ShopSerializer(data=data)
        # 데이터 형식을 JSON 으로 바꿔준다 

        if serializer.is_valid():
            # 만약 실제 데이터베이스 형식대로 맞다 하면 

            serializer.save()
            # serializer 저장한다 
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)










@csrf_exempt
# csrf 는 보안용, front 와 backend 소통을 할때 중간에 바꿔주는 경우가 있기 때문에 보안하기 위해서 보안적인 요소
def menu(request, shop):
    # shop 을 붙이지 않으면 모든 menu 를 호출한다. 
    if request.method == 'GET':
        # 만약 request method 가 get 이라면 

        menu = Menu.objects.filter(shop=shop)        # filter(shop=shop) 이라는 뜻은, 웹 사이트에서 클릭했을 경우 해당되는 메뉴만 호출한다. filter 는 여러가지를 호출할 수 있다. get(shop=shop) 은 하나밖에 안된다.
        # Menu 데이터 베이스는 모든 object 을 다 shop 에다가 저장한다. 

#        serializer = MenuSerializer(menu, many=True)  # many = true 라는 뜻은, menu 가 많아도 상관 안하겠다. 
        # 그리고 그 데이터들은 serializer 통해서 JSON 형태 passing 을 해서 JSON 형태로 변환해서,
        # Serializer 라는 것은, 데이터 베이스가 현재 JSON 형태가 아니기 때문에 그것을 편리하게 보여주기 위해 JSON 형태로 바꿔주는 Seriallizer 를 사용한다 
#        return JsonResponse(serializer.data, safe=False)
        # JSON 형태로 보여 주겠다. 

        return render(request, 'order/menu_list.html', {'Menu_list':menu, 'shop':shop})


    elif request.method == 'POST':
        # 데이터를 추가하는 목적 

        data = JSONParser().parse(request)
        # 데이터에서 JSONParser (JSONParser is the base class to define public API for reading JSON content. It is the most efficient way for reading JSON data.)
        # 어떤 데이터를 추가 할 것인지 JSON 형태 나와있기 때문에 그것을 Parsing 한 다음에 

        serializer = MenuSerializer(data=data)
        # 데이터 형식을 JSON 으로 바꿔준다 

        if serializer.is_valid():
            # 만약 실제 데이터베이스 형식대로 맞다 하면 

            serializer.save()
            # serializer 저장한다 
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)









from django.utils import timezone
@csrf_exempt
# csrf 는 보안용, front 와 backend 소통을 할때 중간에 바꿔주는 경우가 있기 때문에 보안하기 위해서 보안적인 요소
def order(request):

    if request.method == 'POST':
        # 데이터를 추가하는 목적 
        address = request.POST['address']
        # 변수를 지정하기 위한 목적
        # address 이라는 변수에 request.POST['address'] 입력된 주소를 넣기.
        shop = request.POST['shop']
        # 어떤 상점에서 주문을 했는지 알아야 되기때문에 

        food_list = request.POST.getlist('menu')

        order_date = timezone.now()
        shop_item = Shop.objects.get(pk=int(shop))
        # 몇번째 shop 에서 주문을 했으면은 그 shop 의 테이블만 가져오는 형식
        # 예를 들어 http://127.0.0.1:8000/order/menus/3 는 shop_item 이 끝자리 3이다. 

        shop_item.order_set.create(address = address,order_date=order_date,shop = int(shop))
        # 외래 key 를 받는 models 를 생성한다
        # address 를 불러오고 shop 도 불러오고 order_date 도 불러오고 Order_set.create 통해서 데이터 베이스에 쌓고 (shop)


        order_item = Order.objects.get(pk = shop_item.order_set.latest('id').id)
       
        for food in food_list:
            order_item.order_food_set.create(food_name = food)

        return render(request, 'order/success.html')

    elif request.method == 'GET':
        order_list = Order.objects.all()
        return render(request, 'order/order_list.html', {'order_list':order_list})