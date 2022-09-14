from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("",  views.index, name="index"),
    path("add", views.add, name="add"),
    path("about", views.about, name="about"),
#3path("books/add/", views.add_book, name="add_book")
]