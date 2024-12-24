from django.shortcuts import HttpResponse

from rest_framework.views import APIView


# 构建了新的dispatch方法 取代之前的View
# 功能一: 构建新的request对象, 让数据更好管理, 无论是urlencoded 还是json 都变成data:{}
class BookView(APIView):
    def get(self, request):
        print("request", request.query_params)
        return HttpResponse("APIView Get 请求")

    def post(self, request):

        print("data", request.data)
        return HttpResponse("APIView Post 方法 ")
