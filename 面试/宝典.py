# lambda
# lambda 是一个匿名函数
fun=lambda x:x*2 #：左边为输入，右边为输出
print(fun(5))


# sorted(iterable,key)
# iterable为一个要排序的可迭代对象
# key是一个函数地址，iterable中的每一个元素都会传到key函数中，
# 函数的返回值就是这个元素的排序条件
# 例如：

# 求倒数
def fun(x):

    return x*-1
list1 = [1,2,3,4,5]
# 可以实现倒序
print(sorted(list1,key=fun))#输出为[5,4,3,2,1]

# 题目
# 现有字典 d={‘a’:24,’g’:52,’l’:12,’k’:33}请按字典
# 中的 value 值进行排序?
d={'a':6,'b':2,'c':5}
d1=sorted(d.items(),key = lambda x:x[1])
print(d1)


n->基->本->的->h