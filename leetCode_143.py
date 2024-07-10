# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Create the linked list [1, 2, 3, 4, 5]
head = ListNode(1)
current = head
for value in [2, 3, 4, 5]:
    current.next = ListNode(value)
    current = current.next



# class Solution:
#     def reorderList(self, head) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         slow = head
#         # while slow.next:
#         for i in range(5):
#             fast1 = slow.next
#             fast2 = slow
#             print(f'before iteration slow {slow.val} fast {fast2.val} ')
#             while fast1.next :
#                 fast1 = fast1.next
#                 fast2 = fast2.next
#             print(f'fast1 {fast1.val} fast2 {fast2.val}')
#             slow.next = fast1 # linking the last node after the 1st node
#             fast1.next = slow.next # linking the immediate node after the last node
#             slow = fast1.next # moving the pointer to the immediate node
#             fast2.next = None # assigning the final node is to none
#         return head
# sol = Solution()
# sol.reorderList(head)

class Solution:
    def reorderList(self, head) -> None:
        # find the middle of the linked list
        slow, fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reversing the linked list
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge the two halfs
        first,second = head,prev
        while second:
            tmp1 , tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1,tmp2




# Function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

# Print the linked list to verify
print_linked_list(head)
