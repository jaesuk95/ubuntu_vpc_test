from django.urls import path
from order import views

urlpatterns = [
    path('shops/', views.shop, name="shop"),    # name 을 지은 이유는 url 에 이름을 다는것이다 
    path('menus/<int:shop>', views.menu, name="menus"),
    # int:shop 이라는 것은 여기서 shop 이 views.py 에 shop parameter 를 불러온다. 
    path('order/',views.order, name="order")
]