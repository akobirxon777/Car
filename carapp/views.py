from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Car, Like , Savat
from django.shortcuts import get_object_or_404
from django.conf import settings


def cars(request):
    cars = Car.objects.all()
    return render(request, "car.html", {'cars': cars})


def detail_car(request, id):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
         
    car = Car.objects.get(id=id)
    return render(request, "deteil_car.html", {"car": car})


def car_create(request):
    if request.method =='POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('car')
    else:
        form = CarForm()
    return render(request, 'create_car.html', {'form': form})



def delete_car(request, id):
    carlar = get_object_or_404(Car, id=id)
    carlar.delete()
    return redirect('car')

def car_update(request, id):
    car = get_object_or_404(Car, id=id)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car')
    else:
        form = CarForm(instance=car)
    return render(request, 'create_car.html', {'form': form, 'car': car})


 
def register(request):
    return render(request, 'registration.html')




@login_required
def like(request, id):
    car = get_object_or_404(Car, id=id)
    user = request.user

    liked = Like.objects.filter(user=user, car=car).exists()

    if liked:
        # User already liked the car, so unlike it
        Like.objects.filter(user=user, car=car).delete()
        car.like -= 1
        car.save()
        return JsonResponse({'status': 'unlike', 'like_count': car.like})
    else:
        # User has not liked the car yet, so like it
        Like.objects.create(user=user, car=car)
        car.like += 1
        car.save()
        return JsonResponse({'status': 'like', 'like_count': car.like})


















def SavatView(request):
    cart_products = Savat.objects.all()
    count_of_products = len(cart_products)
    price_of_products = sum(i.product.new_price*i.quantity for i in cart_products)
    econom_price = sum((i.product.old_price-i.product.new_price)*i.quantity for i in cart_products)
    total_price = price_of_products+30000
    context = {
        'mahsulotlar': cart_products,
        'count_of_products': count_of_products,
        'econom_price':econom_price,
        'price_of_products': price_of_products,
        'total_price': total_price
    }
    return render(request, 'cart.html', context)


def cart_add(request,product_id):
    product = Car.objects.get(id=product_id)
    savat = Savat.objects.filter(product=product)
    
    if not savat.exists():
        Savat.objects.create(product=product,quantity=1)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        savat1 = savat.first()
        savat1.quantity += 1
        savat1.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
        



def delete_product_cart(request, product_id):
    product = get_object_or_404(Car, pk=product_id)
    savat = Savat.objects.filter(product=product)
    
    if savat.exists():
        savat.delete()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

