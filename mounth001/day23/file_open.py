# r w a r+ w+ a+
# read([size])
# readline([size])
# readlines([sizeint])
# try:
# except Exception as e:
#     print(e)
#
# data=file.read()
# print(data)
# file.close()
file=open('text.py','r')

# while True:
#     data=file.read()
#     print(data)
while True:
    data=file.readlines(20)
    if not data:
        break

    print(data)



