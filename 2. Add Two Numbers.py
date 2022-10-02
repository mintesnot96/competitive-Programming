class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        sumh = ListNode()
        cur_sum = sumh
        before_cur  = None
        while l1 != None or l2 != None:
            left = l1.val if l1 != None else 0
            right = l2.val if l2 != None else 0
            
            cur_sum.next = ListNode()
            cur_sum.next.val = (cur_sum.val + left + right) // 10
            cur_sum.val = (cur_sum.val + left + right) % 10
            before_cur = cur_sum
            cur_sum = cur_sum.next

            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None

        if cur_sum.val == 0:
            before_cur.next = None
            
        return sumh
