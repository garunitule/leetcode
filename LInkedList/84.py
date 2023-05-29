# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        non_duplicates_values = []
        prev_node = None

        while head is not None:
            # nextはここで更新
            next_node = head.next

            # 次ノードの値を取得
            if next_node is None:
                next_node_val = None
            else:
                next_node_val = next_node.val

            # -----前後の重複がないことを確認-----
            # 初回の場合
            if prev_node is None:
                if head.val != next_node_val:
                    non_duplicates_values.append(head.val)
            # 最後の場合
            elif next_node_val is None:
                if head.val != prev_node.val:
                    non_duplicates_values.append(head.val)
            else:
                if prev_node.val != head.val and head.val != next_node_val:
                    non_duplicates_values.append(head.val)
            
            # 更新
            prev_node = head
            head = head.next

        
        answer = None
        while len(non_duplicates_values) > 0:
            answer = ListNode(
                val=non_duplicates_values.pop(),
                next=answer
            )

        return answer

