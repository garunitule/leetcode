# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(val=-1000)
        list_excluded_duplicates = []
        while head is not None:
            if prev.val != head.val:
                list_excluded_duplicates.append(head.val)
            prev = head
            head = head.next
        
        answer = None
        while len(list_excluded_duplicates) > 0:
            answer = ListNode(val=list_excluded_duplicates.pop(), next=answer)
        
        return answer

