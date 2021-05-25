from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.urls import reverse
from django.utils.html import format_html

from typeidea.base_admin import BaseOwnerAdmin
from typeidea.custom_site import custom_site
from .adminforms import *

from .models import *


# Register your models here.

# 关联使用方法，在分类页面关联文章
class PostInline(admin.TabularInline):
    fields = ('title', 'description')
    extra = 1
    model = Post


class CategoryOwnerFilter(admin.SimpleListFilter):
    # 自定义过滤器展示当前用户分类
    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count')
    fields = ('name', 'status', 'is_nav')

    # inlines = [PostInline, ]

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = [
        'title', 'category', 'status',
        'created_time', 'owner', 'operator'
    ]  # 页面展示的字段
    list_display_links = []  # 页面展示的链接
    list_filter = [CategoryOwnerFilter]
    search_fields = ['title', 'category__name']
    save_on_top = True
    actions_on_top = True
    actions_on_bottom = True

    # 编辑页面
    save_on_top = True
    exclude = ['owner']
    '''
    fields = [
        ('category', 'title'),
        'description',
        'status',
        'content',
        'tag',
    ]
    '''
    # fields 与 fieldsets 不可以共存
    fieldsets = (
        ('基础配置', {
            'description': '基础配置描述',
            'fields': (
                ('title', 'category'),
                'status',
            )
        }),
        ('内容', {
            'fields': (
                'description',
                'content',
            )
        }),
       # ('额外信息', {
        #    'classes': ('collapse',),
         #   'fields': ('tag',),
       # }),
    )

    # 字段横向展示
    # filter_horizontal = ('tag', )
    # 字段纵向展示
    filter_vertical = ('tag',)

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )

    operator.short_description = '操作'

    class Media:
        css = {
            'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/"
                    "bootstrap.min.css",),
        }
        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js')


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user',
                    'change_message']
