# 创建节点类
class Node:
    def __init__(self,val,next=None):
        self.val=val #有用数据
        self.next=next#节点关系
#单链表的类
class LinkList:
    #生成对象 表示一个
    def __init__(self):
        self.head=Node(None)
    #初始化
    def init_list(self,iter):
        p=self.head
        for i in iter:
            p.next=Node(i)
            p=p.next
    #遍历打印
    def show(self):
        p=self.head.next
        while p is not None:
            print(p.val)
            p=p.next

    #判断列表是否为空
    def is_empty(self):
        return self.head.next is None
    #清空链表
    def clear(self):
        self.head.next=None
    #尾部插入
    def append(self,val):
        p=self.head
        #p移动到最后一个节点
        while p.next is not None:
            p=p.next
            p.next=Node(val)
    #头部插入
    def head_insert(self,val):
        node=Node(val)
        node.next=self.head.next
        self.head.next=node
    #指定位置插入
    def insert(self,index,val):
        p = self.head
        for i in range(index):
            if p.next is None:
                break
            p=p.next
        node=Node(val)
        node.next=p.next
        p.next=node
    #删除节点（删除第一个val值）

    def delete(self,val):
        p=self.head
        #确定p的位置(停留在待删除节点的前一个）

        while p.next is not None and p.next.val !=val:
            p=p.next
        #分情况讨论
        if p.next is None:
            raise ValueError('x not in link')
        else:
            p.next=p.next.next
    #获取节点值
    def get_







if __name__=='__main__':
        link=LinkList()
        link.init_list(range(5))
        link.show()