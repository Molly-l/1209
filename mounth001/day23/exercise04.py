f=open('/home/tarena/adi1907/mounth001/day23/text','rb')
f01=open('/home/tarena/adi1907/mounth001/day23/text01','wb')
while True:
    #循环读取
    e01=f.read()
    if not e01: #文件结束
        break
    f01.write(e01)
f.close()
f01.close()
