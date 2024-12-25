from django.urls import path, re_path
from sers import views

urlpatterns = [
    path("sers/book/", views.BookView.as_view()),
    re_path("sers/book/(?P<pk>\d+)", views.BookDetailView.as_view()),
]
