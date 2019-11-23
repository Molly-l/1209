import re

# w=re.findall(p,"(abcd)efgh(higk)")
# w=re.findall(r'wo{1,2}?',"wooooooooooo--woo-w")
# w=re.findall(r'-?\d+',"25,-85,75,-66")
# w=re.findall(r'\d+\D\d+\D\d+\D\d+',"192.168.76.35")
w=re.search(r'\d+(\.\d+){3}',"192.168.76.35")
# print(w.group('lkjh'))

s1='ki485kiju@i8k.com'
s3='ki485kiju@i8k.cn'
s2='ki485kiju@i8k.cn'
s=s1+s2+s3
#
p=r'\w+@\w+\.(com|cn)'
# w=re.search(p,s)
# print(w.group())

l=re.finditer(p,s)
print(l)
for i in l:
    print(i.group())

print(re.search(r'(?P<pig>ab)+',"ababababab").group(1))




#re.findall 匹配所有
#re.search  只能匹配第一个