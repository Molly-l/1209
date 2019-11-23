class QueueError(Exception):
    pass
# 创建节点类
class Node:
    def __init__(self,val,next=None):
        self.val = val  #  有用数据
        self.next = next # 节点关系
class LQueue:
    def __init__(self):
        #front 队头
        self.front=self.rear=Node(None)
    def is_empty(self):
        return self.front==self.rear
    def enqueue(self,val):
        self.rear.next=Node(val)
        self.rear=self.rear.next
    def dequeue(self):
        if self.is_empty():
            raise QueueError('')
        self.front=self.front.next
        return self.front.val
