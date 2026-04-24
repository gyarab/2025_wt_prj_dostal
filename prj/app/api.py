from ninja import NinjaAPI, Schema, ModelSchema

from app.models import Food  # Corrected import

api = NinjaAPI()

class Message(Schema):
    message: str

class FoodSchema(ModelSchema):
    class Meta:
        model = Food
        model_fields = "__all__"

@api.get("/foods")
def list_foods(request):
    foods = Food.objects.all()

    return {"foods": [food.name for food in foods]}


@api.get("/foods/{food_id}", response={200: FoodSchema, 404: Message})
def get_food(request, food_id: int):
    try:
        food = Food.objects.get(id=food_id)
        return {"food": food.name}
    except Food.DoesNotExist:
        return 404, {"message": "Food not found"}
