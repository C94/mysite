# -*- coding: UTF-8 -*-
from django.contrib import admin

from .models import Question,Choice

class ChoiceInline(admin.TabularInline):
    # 选择表
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # 改变后台管理界面字段的顺序
    # fields = ['pub_date','question_text']

    # 自定义页面，子标题
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('发布时间', {'fields': ['pub_date']}),
    ]

    # 数据以表格方式显示,was_published_recently调用方法
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 过滤的，类似条件搜索
    list_filter = ['pub_date']
    search_fields = ['question_text']
    # 引入其他表模块
    inlines = [ChoiceInline]



admin.site.register(Choice)     #在管理员后台加载显示模块
admin.site.register(Question,QuestionAdmin)
