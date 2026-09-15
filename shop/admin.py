from django.contrib import admin
from .models import Equipment, Product, Review, WinterBike

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('title',)
    

@admin.register(WinterBike)
class WinterBikeAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('title',)
    

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_sold')
    

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'tag')
# Register your models here.
