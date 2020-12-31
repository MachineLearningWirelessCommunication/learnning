from django.http import HttpResponse


def show_views(request):
    return HttpResponse('这是我的第一个django页面')


def show02(request,year):
    return HttpResponse('show02')


def login(request):
    return HttpResponse('这是登录页面')


def register(request):
    return HttpResponse('这是注册页面')


def index(request):
    return HttpResponse('这是首页')
