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
from rest_framework.viewsets import ViewSet, GenericViewSet, ModelViewSet


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookView(ModelViewSet):
    queryset = Book.objects.all()  # 和GenericAPIView 相关的
    serializer_class = BookSerializers  # 和GenericAPIView 相关的
