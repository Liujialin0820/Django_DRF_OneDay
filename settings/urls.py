from django.urls import path, include
from sers import views

urlpatterns = [
    path("sers/book/", views.BookView.as_view()),
]
