"""
使用进程池拷贝一个目录下所有的文件(普通文件)，实时打印拷贝的百分比进度。
"""
from multiprocessing import Pool,Queue
import os

q = Queue() # 消息队列

# 拷贝文件
def copy_file(file,old_dir,new_dir):
    fr = open(old_dir+file,'rb')
    fw = open(new_dir+file,'wb')
    while True:
        data = fr.read(1024)
        if not data:
            break
        n = fw.write(data) # 写入的字节数，write方法的返回值为写入数据的大小（字节数）
        q.put(n) # 放到消息队列

# 创建进程池
def main():
    #  确定好源目录和备份目录
    path = "/home/tarena/"
    dir = input("输入要拷贝的文件目录:")
    old_dir = path + dir + '/' #源目录绝对路径
    new_dir = path + dir+"-备份/"
    os.mkdir(new_dir)#创建一个新的文件夹
    # 要拷贝的文件列表
    file_list = os.listdir(old_dir)#获取路径下所有文件名

    # 获取文件总大小
    total_size = 0
    for file in file_list:
        total_size += os.path.getsize(old_dir+file)
    print("总共大小：%d M"%(total_size/1024//1024))

    pool = Pool(4)#创建进程池对象，最多同时开启4个进程

    # 添加进程池事件
    for file in file_list:
        pool.apply_async(copy_file,args=(file,old_dir,
                                    new_dir))
    pool.close()

    copy_size = 0 # 已经拷贝的大小
    while copy_size < total_size:
        copy_size += q.get() # 获取队列数量值
        print("拷贝了%.1f%%"%(copy_size/total_size*100))

    pool.join()

if __name__ == '__main__':
    main()