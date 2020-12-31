from django.conf.urls import url
from . import views
urlpatterns = [
    # /music/01-show
    # 响应：这是music中的show的访问路径
    url(r'^01-show/$',views.show01)
]