# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        carry = 0
        while l1 and l2:
            amt = l1.val + l2.val + carry
            node = ListNode(amt % 10)
            carry = amt // 10
            curr.next = node
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            amt = l1.val + carry
            node = ListNode(amt % 10)
            carry = amt // 10
            curr.next = node
            l1 = l1.next
            curr = curr.next
        while l2:
            amt = l2.val + carry
            node = ListNode(amt % 10)
            carry = amt // 10
            curr.next = node
            l2 = l2.next
            curr = curr.next
        if carry:
            node = ListNode(carry)
            curr.next = node
        return head.next
