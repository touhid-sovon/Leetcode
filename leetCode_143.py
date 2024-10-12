# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __iter__(self):
        curr = self
        while curr:
            yield curr.val
            curr = curr.next



# linked list creation
list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

for node in list1:
    print(node)


# # Create the linked list [1, 2, 3, 4, 5]
# head = ListNode(1)
# current = head
# for value in [2, 3, 4, 5]:
#     current.next = ListNode(value)
#     current = current.next
#
#
#
#
# class Solution:
#     def reorderList(self, head) -> None:
#         # find the middle of the linked list
#         slow, fast = head,head.next
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#
#         # reversing the linked list
#         second = slow.next
#         prev = slow.next = None
#         while second:
#             tmp = second.next
#             second.next = prev
#             prev = second
#             second = tmp
#
#         # merge the two halfs
#         first,second = head,prev
#         while second:
#             tmp1 , tmp2 = first.next,second.next
#             first.next = second
#             second.next = tmp1
#             first,second = tmp1,tmp2
#
#
#
#
# # Function to print the linked list
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.val, end=" -> " if current.next else "\n")
#         current = current.next
#
# # Print the linked list to verify
# print_linked_list(head)

class Solution:
    def reorderList(self, head) -> None:
        slow = fast = head

        # finding the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reversing the linked list from the middle
        prev = None
        second = slow.next
        while second is not None:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merging two linked list
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
