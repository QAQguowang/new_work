from django.urls import path
from book.views import index

urlpatterns = [
    path('home/', index)
]