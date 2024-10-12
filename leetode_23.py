from typing import Optional, Any


class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(node):
    curr = node
    while curr:
        print(f'{curr.val} ->',end=" ")
        curr = curr.next
    print("")



class Solution:
    def mergeKLists(self,lists:list[Optional[ListNode]])-> Optional[ListNode]:
        if len(lists) == 0:
            return None
        dummy = ListNode(0)
        curr = dummy
        left = lists[0]
        while left:
            curr.next = left
            curr = curr.next
            left = left.next


        for i in range(1,len(lists)):
            curr = dummy
            right = lists[i]
            left = dummy.next
            while left and right:
                if right.val <= left.val:
                    curr.next = right
                    right = right.next
                else:
                    curr.next = left
                    left = left.next
                curr = curr.next

            while left:
                curr.next = left
                left = left.next
                curr = curr.next
            while right:
                curr.next = right
                right = right.next
                curr = curr.next

        return dummy.next

    "devide and coquer"
    def mergeKLists2(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists)>1:
            already_merged = []

            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1<len(lists) else None
                already_merged.append(self.mergeLinkedList(l1,l2))
            lists = already_merged

        return lists[0]

    def mergeLinkedList(self,L1,L2):
        dummy = ListNode(0)
        curr = dummy

        left = L1
        right = L2

        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        if left:
            curr.next = left
        if right:
            curr.next = right

        return dummy.next





list1 = ListNode(1,ListNode(4,ListNode(5)))
list2 = ListNode(1,ListNode(3,ListNode(4)))
list3 = ListNode(2,ListNode(6))

sol = Solution()

#sol.mergeKLists([list1])


#print_linked_list()
sol.mergeKLists([[]])
# print_linked_list(list1)
