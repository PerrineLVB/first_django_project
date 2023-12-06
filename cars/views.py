from django.shortcuts import render

from cars.models import Car


# Create your views here.
def index(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'index.html', context)

def car_details(request):
    car = Car.objects
    context = {'car': car}
    return render(request, 'car_details.html', context)
