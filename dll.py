class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


def Reverse(head):
    t=head
    while t.next!=NULL:
        t.next,t.prev=t.prev,t.next
    return head
