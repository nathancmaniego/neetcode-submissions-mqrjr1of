# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next
        target = count - n
        i = 0
        curr = head
        if target == 0:
            if curr:
                return curr.next
            else:
                return None
        while curr is not None and i < target:
            print(target)
            prev = None
            prev = curr
            curr = curr.next
            i += 1
        if curr:
            prev.next = curr.next
        return head
        