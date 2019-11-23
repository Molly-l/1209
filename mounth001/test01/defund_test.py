import copy
# def fun (*args,**kwargs):
#     return args[0],**kwargs
#
# tuple01=(1,2)
# dict01={'a':3}
#
# print(fun(tuple01,dict01))
# str01='254635'
# print(str01[::-1])
# dict01={'a':1}
# for k,v in dict01.items():
#     print(k,v)
# for k in dict01:
#     print(k,dict01[k])
#
# for k in dict01.keys():

# for v in dict01.values():

#
# def fun01(a,*args,**kwargs):
#     print(a)
#     print(args)
#     # print(b)
#     # print(d)
#     print(kwargs)
# fun01(2,1,2,b=7,d=5,f=6,g=8)
set01=set()
print(type(set01))
set02=(1,2,3)
set03={1,2,3}
print(set01)
tuple01=()
print(tuple01,'')

print(chr(97))
print(ord('一'))
print(type(789654))

a=r'\nao' \
  r'54o\n'
print('''4545          86            85
54     45        85           8
4555             666              6
955''' )

print(a)
d=a
c=a[:]
b=copy.deepcopy(a)

print(id(a),id(b),id(c),id(d))
print(a is b )

# if i in (1,3,5,7,8,10,11):
# not in