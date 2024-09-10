# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        cur = head.next

        while cur:
            prev.next = ListNode(math.gcd(prev.val, cur.val), cur)
            # prev.next.next = cur
            prev = prev.next.next
            cur = cur.next
        return head