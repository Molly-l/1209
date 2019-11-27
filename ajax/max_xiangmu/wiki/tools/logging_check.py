import jwt
from django.http import JsonResponse

from user.models import UserProfile

TOKEN_KEY='1234567ab'

def logging_check(*methods):#
    def _logging_check(func):#验证是否登录
        def wrapper(request,*args,**kwargs):
            #逻辑判断
            #1 判断当前请求是否需要校验

            if not methods:
                return func(request,*args,**kwargs) #如果没有参数，就返回被装饰的函数
            else:
                if request.method not in methods: #当前的请求方法没在参数数组中
                    return func(request,*args,**kwargs)
                else:
                    # 2 取出token
                    token=request.META.get('HTTP_AUTHORIZATION') #固定的
                    if not token:
                        result={'code':20104,'error':'Please login'}
                        return JsonResponse(result)
                    try: 
                        res=jwt.decode(token,TOKEN_KEY,algorithms='HS256')#解密后可以拿出消息主体内容
                    except Exception as e:
                        result = {'code': 20105, 'error': 'Please login'}
                        return JsonResponse(result)
                    # 登陆成功
                    username=res['username']  #把登陆者的用户名从消息主体拿出来


                    user=UserProfile.objects.get(username=username)  #获取用户

                    login_time = res.get('login_time')
                    if login_time:
                        if login_time != str(user.login_time):
                            result = {'code': 20106, 'error': 'Other people have logined!Please login again'}
                            return JsonResponse(result)
                request.user=user  #给request增加user属性
        
        
        
        
            return func(request,*args,**kwargs)
        return wrapper
    return _logging_check

def get_user_by_request(request):
    #尝试获取用户身份
    token=request.META.get('HTTP_AUTHORIZATION')
    if not token:
        #用户没登录
        return None
    try:
        res = jwt.decode(token, TOKEN_KEY, algorithms='HS256')
    except Exception as e:
        return None
    username=res['username']
    users=UserProfile.objects.filter(username=username)   #通过token中的用户名找用户  
    if not users:
        return None
    return users[0]# 返回的是登录用户
