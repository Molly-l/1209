from django.http import HttpResponse
from django.template import  loader
from django.shortcuts import render

def index1(request):
    #1.通过loader加载模板
    t=loader.get_template('test.html')
    #2.t对象转化成html字符串
    html=t.render()
    #3.将html return 至浏览器
    return HttpResponse(html)

    #return HttpResponse('This is index')


def index(request):
    #render 方案
    dic={'username':'guo','age':18}
    return render(request,'test.html',dic)

def test_p(request):
    #测试页面传参
    dic={}
    dic['lst']=['小白',['小明'],['小亮']]
    dic['dict']={'username':'guo','age':18}
    dic['calss_obj']=Dog
    dic['say_hi']=say_hi
    dic['number']=0
    return render(request, 'test_p.html', dic)

class Dog:
    def say(self):
        return 'hahaha'
def say_hi():
    return 'say_hi'

def test_if(request):
    x=request.GET.get('x',0)
    dic={'x':x}
    return render(request, 'test_if.html', dic)

def math(request):
    if request.method=='GET':#获取浏览器的请求方法
        return render(request, 'math.html')  #shortcuts模块中的方法，可以用来加载模板（写好的页面）
    elif request.method=='POST':
        #浏览器会用from POST请求提交如下数据
        #x=x_val&op=op_val&y=y_val


        #from text框 空提交时 浏览器会带上具体text框、
        #的name及空值一并提交到服务器
        x=request.POST.get('x')#取值，浏览器发过来的
        if not x:
            error='Please give me x!'
            dic={'error':error}
            return render(request, 'math.html', dic)
        try:
            x=int(x)
        except Exception as e:
            print('error')
            try:
                x = int(float(x))
            except Exception as e:
                print('error')


        op = request.POST.get('op')
        # dic['op'] = op
        y= int(request.POST.get('y'))
        # dic['y']=y

        # n=0
        if op=='add':
            n=x+y
        elif op=='sub':
            n=x-y
        elif op=='mul':
            n=x*y
        elif op=='div':
            n=x/y
        return render(request, 'math.html', locals())#locals()返回当前函数内所有局部变量形成的字典（键为变量名，值为内容）


def test_for(request):
    dic = ['小白', ['小明'], ['小亮']]
    return render(request, 'test_for.html', locals())

def shebao(request):
    # if request.method == 'GET':  # 获取浏览器的请求方法
    #     return render(request, 'money.html')  # shortcuts模块中的方法，\
    #                                               可以用来加载模板（写好的页面）
    # elif request.method == 'POST':
    #     base=request.POST.get('base')  # 取值，浏览器发过来的
    #     if not base:
    #         error = 'Please give me base!'
    #         dic = {'error': error}
    #         return render(request, 'money.html', dic)
    # try:
    #     base = float(base)
    # except Exception as e:
    #     print('error')
    base = float(request.POST.get('base'))

    if base<3082:
        base=3082
    elif base>23118:
        base=23118

    old_yl=base*0.08
    return render(request, 'shebao.html', locals())  #   4

def money(request):

    return render(request, 'money.html', locals())  #  1