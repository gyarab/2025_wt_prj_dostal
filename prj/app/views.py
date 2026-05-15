from django.shortcuts import render
from .models import Food

def render_home(request):
    return render(request, 'home.html')
def render_food_database(request):
    search_query = request.GET.get('q', '')
    if search_query:
        foods = Food.objects.filter(name__icontains=search_query)
    else:
        foods = Food.objects.all()
    
    return render(request, 'food_database.html', {'foods': foods, 'search_query': search_query})

def render_api_playground(request):
    return render(request, 'api_playground.html')
