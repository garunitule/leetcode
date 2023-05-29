# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        added_nums = []
        leading_val = 0
        while l1 is not None or l2 is not None or leading_val != 0:
            added_num = leading_val
            if l1 is not None:
                added_num += l1.val
            if l2 is not None:
                added_num += l2.val

            leading_val = added_num // 10
            added_num %= 10
            added_nums.append(added_num)

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        answer = None
        while len(added_nums) > 0:
            answer = ListNode(val=added_nums.pop(), next=answer)
        return answer