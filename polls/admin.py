# -*- coding: UTF-8 -*-
from django.contrib import admin

from .models import Choice
from .models import Question

admin.site.register(Choice)     #在管理员后台加载显示模块
admin.site.register(Question)