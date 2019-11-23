# 字符串  split()分裂  join()  strip()删除头尾,无参数默认删除空格  format()格式  replace(被替换,新)替换
str = "Line1-abcdef \nLine2-abc \nLine4-abcd"
print(str.split( ))       # 以空格为分隔符，包含 \n
print(str.split(' ', 1 )) # 以空格为分隔符，分隔成两个

str = "-"
seq = ("a", "b", "c") # 字符串序列
print(str.join( seq ))

str = "    1212bcru21noob3       "
print(str.strip()) # 字符序列为 12
print(str.replace('abcrun',''))


print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的


# open()打开 read()读  write()写

