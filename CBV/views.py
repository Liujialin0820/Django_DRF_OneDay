from django.shortcuts import render, HttpResponse

# Create your views here.


def book(request):
    if request.method == "GET":
        return HttpResponse("get")
    else:
        return HttpResponse("others")
