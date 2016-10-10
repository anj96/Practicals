class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

    def __str__(self):
        return str(self.data)

def pr_list(node):
    while node:
        print( node, end='')
        node = node.next
def ReversePrint(node):
    if node==None: return
    head=node
    tail=node.next
    ReversePrint(tail)
    print(head, end=' ')
n1=Node(1)
n2=Node(2)
n1.next=n2
n3=Node(3)

ReversePrint(n1)