import time
f=open('log.txt','a+')
f.seek(0)
n=1
for line in f:
    n+=1
num01=n
while True:
    f.write(str(num01)+'.  '+time.ctime()+'\n')
    time.sleep(1)
    num01+=1


