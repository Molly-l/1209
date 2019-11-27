import json
# env='kji'
env={'juju':558}
print(type(env))#type()查看数据类型
data = json.dumps(env)#打包数据
print(type(data))
print(data)
message = json.loads(data)#解压
print(type(message))
print(message)
