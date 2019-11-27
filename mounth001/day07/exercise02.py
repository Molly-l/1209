# s1={1,2,3}
# s2={1,2,4}
# s3=s1&s2
# print(s3)
#
# s4=s1|s2
# print(s4)
#
# s5=s1-s2
# print(s5)
#
# s6=s2-s1
# print(s6)
#
# s7=s1^s2
# print(s7)
#
# s8=s1<s2
# print(s8)
#
# s9=s1==s2
# print(s9)

jingli={'曹操','刘备','孙权'}
jishu={'曹操','刘备','关羽','张飞'}
s01=jingli&jishu
s02=jingli-jishu
s03=jishu-jingli
s04={
    jingli:{'曹操','刘备','孙权'},
    jishu:{'曹操','刘备','关羽','张飞'}
}
print(len([jingli]&s04[jishu]))
print('张飞' in s04[jingli])
print(s04[jingli]|s04[jishu])
print(s04[jingli]^s04[jishu])