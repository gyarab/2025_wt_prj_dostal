from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.FloatField()
    protein = models.FloatField()   
    carbs = models.FloatField()    
    fats = models.FloatField()     
    sugar = models.FloatField(null=True)
    saturated_fats = models.FloatField(null=True)

    def __str__(self):
        return self.name

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    amount = models.FloatField() 
    date = models.DateTimeField()

    def __str__(self):
        user_name = self.user.username if self.user else "No User"
        return f"{user_name} - {self.food.name} ({self.date})"