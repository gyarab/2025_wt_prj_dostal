from django.contrib import admin
from django.urls import path

from app import views
from app.api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.render_home, name="home"),
    path('food_database/', views.render_food_database, name="food_database"),
    path('api_playground/', views.render_api_playground, name="api_playground"),
    path("api/", api.urls)
]
