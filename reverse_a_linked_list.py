class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = Node()
        while node:
            yield node
            node = node.next


class Solution:
    def reverseList(self, head):


















