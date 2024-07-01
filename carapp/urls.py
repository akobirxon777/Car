from django.urls import path
from .views import cars, detail_car, car_create,delete_car,car_update



urlpatterns = [
    path('', cars, name="car"),
    path('car/<int:id>/', detail_car, name="car_detail"),
    path('car/create', car_create, name= 'create'),
    path('car/delete/<int:id>/', delete_car, name= 'delete_car'),
    path('car/update/<int:id>/', car_update, name="car_update"),
]