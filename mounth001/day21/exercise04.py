class QueueError(Exception):
    pass
class SQueue:
    def __init__(self):
        # 标记顶位置
        self._elems = []

    def is_empty(self):
        return self._elems == []
    #入队
    def enqueue(self,val):
        self._elems.append(val)
    #出对
    def dequeue(self):
        if not self._elems:
            raise QueueError('Queue is elem')
        return self._elems.pop(0)


# list01=[]
# list02=[]
# form squeue import
#     def __init__(self):
#
#     def switch_order(self):
#         p=self.head
