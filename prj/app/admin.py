from django.contrib import admin
from .models import Food, Meal

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories', 'protein', 'carbs', 'fats')

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('user', 'food', 'amount', 'date')