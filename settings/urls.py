from django.urls import path, include
from CBV.views import book

urlpatterns = [
    path("book/", book),
]
