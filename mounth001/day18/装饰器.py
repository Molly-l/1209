# 装饰器的作用：在不修改原函数的情况下，为函数增加新功能
#闭包的三个条件：1.外部函数必须要有内部函数
              #2.外部函数的返回值必须是内部函数
              #3.内部函数调用外部函数的变量

def print_func_name(func):
    # *args 原函数参数可以无限制
    def wrapper(*args,**kwargs):
        print(func.__name__)# 打印函数名称
        # return 原函数返回值
        return func(*args,**kwargs)# 调用函数
    return wrapper
#
# @print_func_name
# def enter_background():
#     print('进入后台')
#     return 1
#
# @print_func_name
# def delete_order():
#     print("删除订单")
#     return 2

# print(say_hello())#1
# print(say_goodbye("qtx"))#2



def fun_time(func):
    # *args 原函数参数可以无限制
    def wrapper(*args,**kwargs):
        print(func.__name__)# 打印函数名称
        # return 原函数返回值
        return func(*args,**kwargs)# 调用函数
    return wrapper

@fun_time
def fun01():
    print('进入后台')
    return 1
fun01()
@fun_time
def delete_order():
    print("删除订单")
    return 2
