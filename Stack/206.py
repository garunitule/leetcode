# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        import queue
        vals = queue.Queue()
        while head is not None:
            vals.put(head.val)
            head = head.next
        
        ans = None
        while not vals.empty():
            val = vals.get()
            ans = ListNode(val=val, next=ans)
        return ans
    

# loopが1個で済む解法
# 発想としては、n=ListNode(val=val, next=n)で作るのが楽なので
# ListNodeを作る際は、子から作りたい
# この場合、valは親から子へ順にたどりたいので、headから順に辿れば良い
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        # 逆順になった連結リスト
        prev = None
        # どんどん次へ進む
        curr = head
        # Run a loop till curr points to NULL...
        while curr:
            # 次の連結リストノードを保持
            next = curr.next
            # nextをprevにすることで、currが現時点での逆順の連結リストになる
            curr.next = prev
            # ので、prevを代入する
            prev = curr
            # currを次のノードに更新する
            curr = next
        return prev       # Return the prev pointer to get the reverse linked list...