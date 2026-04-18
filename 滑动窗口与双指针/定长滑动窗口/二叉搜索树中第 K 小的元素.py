class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal k, ans
            if node is None or k <= 0:
                return
            dfs(node.left)  # 左
            k -= 1
            if k == 0:
                ans = node.val  # 根
            dfs(node.right)  # 右
        dfs(root)
        return ans

