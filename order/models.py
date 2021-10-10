from django.db import models

class Shop(models.Model):
    Shop_name = models.CharField(max_length=20)
    Shop_address = models.CharField(max_length=40)
    # shop database 테이블 안에는 이름과 주소가 입력, pk 는 자동으로 생성 

class Menu(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    # menu 는 Shop 상점에 포함 되기 때문에 상속받는다. 
    # ForeignKey 는 Shop 클래스부터 갖고 온다. 
    # Shop 에 지명받은 id 는 다 함께 지워진다. (cascade)
    food_name = models.CharField(max_length=20)

class Order(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    # order 도 shop 에서 주문하는 것이기 때문에, shop 으로부터 상속받는다. 
    order_date = models.DateTimeField('date ordered')
    address = models.CharField(max_length=40)
    # 주문을 한 날짜
    estimated_time = models.IntegerField(default=-1)
    # 주문 시간, -1 이유는 주문을 하기 전에는 -1 로 설정한다. 그리고 주문을 입력하고 예상 시간을 입력하면 default 가 시간으로 변경된다. 
    deliver_finish = models.BooleanField(default=0)

class Order_food(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=20)