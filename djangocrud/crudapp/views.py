from django.shortcuts import render
from .models import Car
from django.contrib import messages
from django.db.models import Q

def index(request):
    cars = Car.objects.all()
    query = ""

    if request.method == "POST":
        if "add" in request.POST:
            name = request.POST.get("name")
            brand = request.POST.get("brand")
            model = request.POST.get("model")
            price = request.POST.get("price")
            Car.objects.create(
                name=name,
                brand=brand,
                model=model,
                price=price
            )
            messages.success(request, "Car Added Successfully")

        elif "update" in request.POST:
            id = request.POST.get("id")
            name = request.POST.get("name")
            brand = request.POST.get("brand")
            model = request.POST.get("model")
            price = request.POST.get("price")

            update_car = Car.objects.get(id=id)
            update_car.name = name
            update_car.brand = brand
            update_car.model = model
            update_car.price = price
            update_car.save()

            messages.success(request, "Car Updated Successfully")

        elif "delete" in request.POST:
            id = request.POST.get("id")
            Car.objects.get(id=id).delete()

            messages.success(request, "Car Deleted Successfully")

        elif "search" in request.POST:
            query = request.POST.get("searchquery")
            cars = Car.objects.filter(Q(name__icontains=query) | Q(brand__icontains=query) | Q(model__icontains=query) | Q(price__icontains=query))

    context = {"cars": cars, "query": query}
    return render(request, "index.html", context=context)
