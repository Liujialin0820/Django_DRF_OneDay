from django.shortcuts import render, HttpResponse

# Create your views here.
from .models import Book
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book


class BookView(GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

    def get(self, request):
        self.get_serializer(instance=self.get_queryset(), many=True)
