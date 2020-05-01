from django.urls import path
from .views import home, deleteItem

urlpatterns = [
    path("",home, name="home-page"),
    path("deleteItem/<int:pk>", deleteItem, name="deleteItem"),
]