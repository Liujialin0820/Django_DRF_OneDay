from django.urls import path, re_path
from sers import views

urlpatterns = [
    path(
        "sers/book/",
        views.BookView.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    re_path(
        "sers/book/(?P<pk>\d+)",
        views.BookView.as_view(
            {
                "get": "get_object",
                "update": "update_object",
                "delete": "delete_object",
            }
        ),
    ),
]
