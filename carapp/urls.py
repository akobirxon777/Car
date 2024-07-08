from django.urls import path
from .views import cars, detail_car, car_create,delete_car,car_update, like, delete_product_cart, cart_add, SavatView



urlpatterns = [
    path('', cars, name="car"),
    path('car/<int:id>/', detail_car, name="car_detail"),
    path('car/create', car_create, name= 'create'),
    path('car/delete/<int:id>/', delete_car, name= 'delete_car'),
    path('car/update/<int:id>/', car_update, name="car_update"),
    path('like/<int:id>/', like, name='like'),
    path('cart/delete/<int:product_id>', delete_product_cart, name='delete_product'),
    path('cart/add/<int:product_id>', cart_add, name='cart_add'),
    path('cart/', SavatView, name='cart'),
]