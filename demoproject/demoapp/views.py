from unittest import result

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def demo(request):
    return render(request, "indexxx.html")


def add(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    res1 = x + y
    return render(request, "result.html", {'result': res1})


def plus(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    res2 = x + y
    return render(request, "result.html", {'result': res2})


def minus(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    res3 = x - y
    return render(request, "result.html", {'result': res3})


def multy(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    res4 = x * y
    return render(request, "result.html", {'result': res4})


def division(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    res5 = x / y
    return render(request, "result.html", {'result': res5})
