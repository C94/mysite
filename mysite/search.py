# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response

#表单提交
def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    request.encoding = 'utf-8'
    if 'username' in request.GET:
        message = '搜索的内容为：' + request.GET['username']
    else:
        message = '提交内容为空'
    return HttpResponse(message)
