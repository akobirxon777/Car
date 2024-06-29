from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm
from django.shortcuts import get_object_or_404


def cars(request):
    cars = Car.objects.all()
    return render(request, "car.html", {'cars': cars})


def detail_car(request, id):
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

def login(request):
    return render(request, 'login.html')