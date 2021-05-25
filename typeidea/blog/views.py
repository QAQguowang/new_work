from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from blog.models import Tag, Post, Category
from config.models import SideBar


def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None

    if tag_id:
        _post_list, tag = Post.get_by_tag(tag_id)
    elif category_id:
        _post_list, category = Post.get_by_category(category_id)
    else:
        _post_list = Post.latest_posts()

    context = {
        'category': category,
        'tag': tag,
        'post_list': _post_list,
        'sidebars': SideBar.get_all(),
    }
    context.update(Category.get_navs())
    return render(request, 'blog/list.html', context=context)


def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None
    context = {
        'post' : post,
        'sidebars' : SideBar.get_all()
    }
    context.update(Category.get_navs())
    return render(request, 'blog/detail.html', context=context)
