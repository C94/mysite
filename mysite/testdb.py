# -*- coding: utf-8 -*-
from django.http import HttpResponse

from TestModel.models import Test

def testdb(request):
    response = ""
    response1 = ""
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM

    # 查询所有数据
    list = Test.objects.all()
    response2 = Test.objects.filter(id=1)

    for var in list:
        response1 += var.name + " "
    response = response1

    # 添加数据
    # test1 = Test.objects.get(id=1)
    # test1.name = 'php'
    # test1.save()

    # 删除数据
    Test.objects.get(id=4).delete()
    return HttpResponse("<p>" + response + "</p>")
