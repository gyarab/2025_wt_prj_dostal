from ninja import NinjaAPI, Schema, ModelSchema
from typing import List
from .models import Food, Meal

api = NinjaAPI()


class MessageSchema(Schema):
    message: str


# ---Food Schemas---

class FoodSchema(ModelSchema):
    class Meta:
        model = Food
        fields = "__all__"


class FoodCreateSchema(ModelSchema):
    class Meta:
        model = Food
        fields = "__all__"
        exclude = ["id"]


class FoodListingSchema(Schema):
    count: int
    results: List[FoodSchema]

# ---Meal Schemas---

class MealSchema(Schema):
    id: int
    user: str | None
    food: str | None
    amount: int
    date: str


class MealListingSchema(Schema):
    count: int
    results: List[MealSchema]


class MealCreateSchema(Schema):
    amount: int
    food_id: int
    date: str

class MealUpdateSchema(Schema):
    amount: int | None = None
    food_id: int | None = None
    date: str | None = None

# ---Food endpoints---

@api.get("/food", response=FoodListingSchema)
def get_foods(request):
    foods = Food.objects.all()
    return {
        "count": foods.count(),
        "results": foods
    }


@api.get("/food/{food_id}", response={200: FoodSchema, 404: MessageSchema})
def get_food(request, food_id: int):
    try:
        food = Food.objects.get(id=food_id)
        return food
    except Food.DoesNotExist:
        return 404, {"message": "Food not found"}


@api.post("/food", response={201: FoodSchema, 400: MessageSchema})
def create_food(request, data: FoodCreateSchema):
    try:
        food = Food.objects.create(**data.dict())
        return 201, food
    except Exception:
        return 400, {"message": "Failed to create food"}


@api.put("/food/{food_id}", response={200: FoodSchema, 404: MessageSchema})
def update_food(request, food_id: int, data: FoodSchema):
    try:
        food = Food.objects.get(id=food_id)
        for attr, value in data.dict().items():
            setattr(food, attr, value)
        food.save()
        return food
    except Food.DoesNotExist:
        return 404, {"message": "Food not found"}
    except Exception:
        return 400, {"message": "Failed to update food"}


# ---Meal endpoints---

@api.get("/meal", response=MealListingSchema)
def get_meals(request):
    meals = Meal.objects.all()
    results = []

    for meal in meals:
        results.append({
            "id": meal.id,
            "user": meal.user.first_name if meal.user else None,
            "food": meal.food.name if meal.food else None,
            "amount": meal.amount,
            "date": str(meal.date),
        })

    return {
        "count": len(results),
        "results": results
    }


@api.get("/meal/{meal_id}", response={200: MealSchema, 404: MessageSchema})
def get_meal(request, meal_id: int):
    try:
        meal = Meal.objects.get(id=meal_id)
        return {
            "id": meal.id,
            "user": meal.user.first_name if meal.user else None,
            "food": meal.food.name if meal.food else None,
            "amount": meal.amount,
            "date": str(meal.date),
        }
    except Meal.DoesNotExist:
        return 404, {"message": "Meal not found"}


@api.post("/meal", response={201: MealSchema, 400: MessageSchema})
def create_meal(request, data: MealCreateSchema):
    try:
        food = Food.objects.get(id=data.food_id)

        meal = Meal.objects.create(
            amount=data.amount,
            food=food,
            date=data.date,
        )

        return 201, {
            "id": meal.id,
            "user": meal.user.first_name if meal.user else None,
            "food": meal.food.name if meal.food else None,
            "amount": meal.amount,
            "date": str(meal.date),
        }

    except Food.DoesNotExist:
        return 400, {"message": "Invalid food ID"}
    except Exception:
        return 400, {"message": "Failed to create meal"}
    
@api.put("/meal/{meal_id}", response={200: MealSchema, 404: MessageSchema, 400: MessageSchema})
def update_meal(request, meal_id: int, data: MealUpdateSchema):
    try:
        meal = Meal.objects.get(id=meal_id)

        if data.amount is not None:
            meal.amount = data.amount

        if data.food_id is not None:
            try:
                food = Food.objects.get(id=data.food_id)
                meal.food = food
            except Food.DoesNotExist:
                return 400, {"message": "Invalid food ID"}

        if data.date is not None:
            meal.date = data.date

        meal.save()

        return {
            "id": meal.id,
            "user": meal.user.first_name if meal.user else None,
            "food": meal.food.name if meal.food else None,
            "amount": meal.amount,
            "date": str(meal.date),
        }

    except Meal.DoesNotExist:
        return 404, {"message": "Meal not found"}
    except Exception as e:
        return 400, {"message": "Failed to update meal"}