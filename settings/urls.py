from django.urls import path, re_path
from sers import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("sers/book", views.BookView)


urlpatterns = [
    #     path(
    #         "sers/book/",
    #         views.BookView.as_view(
    #             {
    #                 "get": "list",
    #                 "post": "create",
    #             }
    #         ),
    #     ),
    #     re_path(
    #         "sers/book/(?P<pk>\d+)",
    #         views.BookView.as_view(
    #             {
    #                 "get": "retrieve",
    #                 "put": "update",
    #                 "delete": "destroy",
    #             }
    #         ),
    #     ),
]

urlpatterns += router.urls
