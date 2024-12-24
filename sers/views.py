from django.shortcuts import render, HttpResponse

# Create your views here.
from rest_framework.views import APIView
from .models import Book
from rest_framework import serializers
from rest_framework.response import Response


class BookSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=32)
    price = serializers.IntegerField()
    pub_date = serializers.DateField()


class BookView(APIView):
    def get(self, request):
        # 获取了一个queryset对象, 要做序列化
        book_list = Book.objects.all()
        # 序列化
        serializer = BookSerializers(instance=book_list, many=True)
        #  序列化的过程就是 把book_list 里面的东西遍历 ,生成json结构的字典
        #  字典内容根据serializers里的处理
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        # 数据反序列化
        serializer = BookSerializers(data=request.data)
        # 校验数据
        if serializer.is_valid():
            # 数据校验通过
            Book.objects.create(**serializer.validated_data)
            return Response(serializer.data)
        # 校验失败
        else:
            return Response(serializer.errors)