from rest_framework import serializers
from order.models import Shop, Menu, Order, Order_food

class ShopSerializer(serializers.ModelSerializer):
# ShopSerializer 같은 경우에는 serializers 안에있는 ModelSerializer 이라는 것을 받아가주고 그것을 바탕으로 사용한다. 
    class Meta:
        model = Shop
        # 데이터 베이스는 Shop
        fields = '__all__'
        # 어떤 필드를 JSON 으로 보여줄거냐 선택 



class MenuSerializer(serializers.ModelSerializer):
# ShopSerializer 같은 경우에는 serializers 안에있는 ModelSerializer 이라는 것을 받아가주고 그것을 바탕으로 사용한다. 
    class Meta:
        model = Menu
        # 데이터 베이스는 menu
        fields = '__all__'
        # 어떤 필드를 JSON 으로 보여줄거냐 선택 