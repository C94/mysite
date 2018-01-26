# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context = {}
    context['hello'] = '你好，世界'
    return  render(request, 'hello.html',context)
    # return HttpResponse('hello world')

def index(request):
    return HttpResponse("hello, this is mysite/view.py")

