class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        st = []  # 单调栈（节点值，节点下标）
        while head:
            while st and st[-1][0] < head.val:
                ans[st.pop()[1]] = head.val  # 用当前节点值更新答案
            st.append((head.val, len(ans)))  # 当前 ans 的长度就是当前节点的下标
            ans.append(0)  # 占位
            head = head.next
        return ans

