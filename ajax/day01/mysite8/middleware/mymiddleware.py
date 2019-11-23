from django.utils.deprecation import MiddlewareMixin

class MyMw(MiddlewareMixin):
    def process_request(self,request):#进urls之前
        #
        print('MyMw process_request do ---')
        return  None
        #return response 请求终止，直接响应
    def process_view(self,request,callback,callback_args,callback_akwrgs):
        #进入views视图之前调用
        #返回值同上
        print('MyMw process_request do ---')
        return #
    def process_response(self,request,response):
        #响应返回给浏览器

        print('MyMw process_request do ---')
        return response
    
    
class MyMw2(MiddlewareMixin):
    def process_request(self,request):
        #
        print('MyMw2 process_request do ---')
    def process_view(self,request,callback,callback_args,callback_akwrgs):
        #进入views试图之前调用
        #返回值同上
        print('MyMw2 process_request do ---')
    def process_response(self,request,response):
        #响应返回给浏览器

        print('MyMw2 process_request do ---')
        return response