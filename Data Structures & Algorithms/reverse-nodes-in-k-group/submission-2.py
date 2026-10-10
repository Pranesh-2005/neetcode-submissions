# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        grpprev = dummy
        def getkth(cur,k):
            while cur and k>0:
                cur = cur.next
                k -= 1
            return cur
        while True:
            kth = getkth(grpprev,k)
            if not kth:
                break
            grpnxt = kth.next
            prev,cur = kth.next, grpprev.next
            while cur != grpnxt:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            temp = grpprev.next
            grpprev.next = kth
            grpprev = temp
        return dummy.next
