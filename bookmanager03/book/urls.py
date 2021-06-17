from django.urls import path
from django.urls.converters import register_converter
from book.views import *

#定义转换器
class MobileCoverter:
    regex = '1[3-9]\d{9}'
    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return str(value)

#注册转换器
register_converter(MobileCoverter, 'mobile_number')

urlpatterns = [
    path('index/', index),
    path('<int:city_id>/<int:shop_id>', shop),
    path('register/', register),
    path('json/', body_request),
    path('<int:mobile>', body_request),
    path('res/', response),
    #使用转换器
    path('<mobile_number:mobile>/', get_mobile),
    path('set_cookie/', set_cookie),
    path('get_cookie/', get_cookie),
    path('set_session/', set_session),
    path('get_session/', get_session),
    path('login/', LoginView.as_view()),
]