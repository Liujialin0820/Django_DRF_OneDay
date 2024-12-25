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


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class BookDetailView(
    GenericAPIView,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy()
