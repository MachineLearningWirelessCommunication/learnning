from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def show01(request):
    return HttpResponse('这是music中的show的访问路径')
