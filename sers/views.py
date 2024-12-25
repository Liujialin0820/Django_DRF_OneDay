from django.shortcuts import render, HttpResponse

# Create your views here.
from .models import Book
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ViewSet


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookView(ViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

    def get_all(self, request):
        return Response("查看所有资源")

    def add_object(self, request):
        return Response("添加资源")

    def get_object(self, request, pk):
        return Response("查看单一资源")

    def update_object(self, request, pk):
        return Response("更新单-资源")

    def delete_object(self, request, pk):
        return Response("删除单一资源")
