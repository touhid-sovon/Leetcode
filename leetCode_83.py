#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode()

class Solution:
    def deleteDuplicates(self, head):
        slow = head
        fast = head.next

        while fast.next is not None:
            if slow.val == fast.val:
                fast = fast.next
                slow.next = fast.val
            else:
                slow = slow.next
                fast = fast.next

        return slow

