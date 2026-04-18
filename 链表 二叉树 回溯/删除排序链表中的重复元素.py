class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        cur = head
        while cur.next:  # 看看下个节点……
            if cur.next.val == cur.val:  # 和我一样，删！
                cur.next = cur.next.next
            else:  # 和我不一样，移动到下个节点
                cur = cur.next
        return head

。