class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        s = set(to_delete)
        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if node is None: return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.val not in s: return node
            if node.left: ans.append(node.left)
            if node.right: ans.append(node.right)
            return None
        if dfs(root): ans.append(root)
        return ans

