from mounth001.day21.exercise04 import SQueue


class Node:
    def __init__(self, val, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
class Bitree:
    def __init__(self):
        self.root=Node(None)
    # 先序遍历
    def preOrder(self,node):
        if node is None:
            return
        print(node.val)
        self.preOrder(node.left)
        self.preOrder(node.right)
    # 中序遍历
    def inOrder(self,node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node.val)
        self.inOrder(node.right)
    # 后序遍历
    def posOrder(self,node):
        if node is None:
            return
        self.posOrder(node.left)
        self.posOrder(node.right)
        print(node.val)
    #层序遍历
    def levelOrder(self, node):
        s01=SQueue()
        s01.enqueue(node)
        while s01.is_empty() is False:
            w01=s01.dequeue()
            print(w01.val)
            if w01.left is not None:
                s01.enqueue(w01.left)
            if w01.right:
                s01.enqueue(w01.right)




tree=Bitree()
b=Node('b')
c=Node('c')
a=Node('a')
tree.root=a
a.left=b
a.right=c
tree.preOrder(tree.root)
tree.levelOrder(tree.root)