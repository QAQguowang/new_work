from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from django.views.generic import ListView

from blog.views import CommonViewMixin
from config.models import Link


class LinkListView(CommonViewMixin, ListView):
    queryset = Link.objects.filter(status=Link.STATUS_NORMAL)
    template_name = 'config/links.html'
    context_object_name = 'link_list'