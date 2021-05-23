from django.contrib import admin

from typeidea.base_admin import BaseOwnerAdmin
from .models import *


# Register your models here.

@admin.register(Comment)
class CommentAdmin(BaseOwnerAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')
