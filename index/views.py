from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from util import test1202
def home(request):


    ret = test1202.getMatch()
    print(ret)
    name = "Hello world!"
    number = 101
    lst = [1, 2, 3, 4, 5]
    dic = {"name": "eric", "job": "teacher"}
    context = {
        "nba": ret,
        "name": name,
        "num": number,
        "lst": lst,
        "dic": dic,   # 键对应的是模板里的名字，值对应的是上面定义的值
    }
    return render(request,'index/home.html',context=context)
