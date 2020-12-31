"""DjangoDemo01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views


urlpatterns = [
    # http://127.0.0.1:8000/admin/
    url(r'^admin/', admin.site.urls),  # 主路由
    # http://127.0.0.1:8000/01-show/   这是我的第一个django页面
    url(r'^01-show/$',views.show_views),
    # http://127.0.0.1:8000/login/   这是登录页面
    url(r'^login/$', views.login),
    # http://127.0.0.1:8000/register/   这是注册页面
    url(r'^register/$', views.register,name='注册'),
    # http://127.0.0.1:8000/   这是首页
    url(r'^$', views.index),
    url(r'^02-show/(\d{4})/$', views.show02),
]

# app   music
urlpatterns += [
    # 判断访问路径如果以  music/ 开始的话，则转交给music应用中的urls去处理
    url(r'^music/',include('music.urls')),
]
