from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect
import json
import re


# Create your views here.

def index(request):
    return HttpResponse('ok')


def shop(request, city_id, shop_id):
    query_parpams = request.GET
    value = query_parpams.getlist('hello')

    return HttpResponse('success')


def register(request):
    data = request.POST
    print(data)
    return HttpResponse('ok')


def body_request(request):
    print(request.META)
    body = request.body
    body_dict = json.loads(body.decode())
    print(body_dict)
    return HttpResponse('success')


def get_mobile(request, mobile):
    print(mobile)
    return redirect('www.baidu.com')


def response(request):
    info = {
        'name': 'haha',
        'address': 'USA'
    }

    list = [
        {'name': '1', 'address': 'USA'},
        {'name': '1', 'address': 'USA'},
    ]

    res = JsonResponse(data=list, safe=False)
    return res


# cookie流程
def set_cookie(request):
    username = request.GET.get('username')
    response = HttpResponse('set_cookie')
    response.set_cookie('name', username, max_age=10)
    return response


def get_cookie(request):
    username = request.COOKIES.get('name')
    response = HttpResponse(username)
    return response

#session流程
def set_session(request):
    username = request.GET.get('username')
    request.session['user_id'] = 1
    request.session['user_name'] = username

    return HttpResponse('set_session')

def get_session(request):
    user_id = request.session.get('user_id')
    user_name = request.session.get('user_name')
    content = '{},{}'.format(user_id, user_name)
    return HttpResponse(content)

