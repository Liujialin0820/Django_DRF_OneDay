from django.urls import path, include
from CBV.views import BookView

urlpatterns = [
    path("book/", BookView.as_view()),
]
