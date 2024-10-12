from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head:Optional[ListNode], n: int) -> [ListNode]:
        temp = ListNode(0, head)
        left = temp
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next
        return temp.next


''' Another solution'''


class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        left = head
        right = head

        # Move the right pointer n steps ahead
        while n > 0 and right:
            right = right.next
            n -= 1

        # If right is None, it means we need to remove the head node
        if not right:
            return head.next

        # Move both pointers until right is at the last node
        while right and right.next:
            right = right.next
            left = left.next

        # Skip the N-th node from the end
        left.next = left.next.next

        return head