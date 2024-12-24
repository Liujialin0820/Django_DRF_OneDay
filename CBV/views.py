from django.shortcuts import HttpResponse
from django.views import View


class BookView(View):
    def get(self, request):
        return HttpResponse("View Get 请求")

    def post(self, request):
        return HttpResponse("Post 方法 ")
