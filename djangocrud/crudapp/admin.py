from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarsAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "brand", "model", "price"]