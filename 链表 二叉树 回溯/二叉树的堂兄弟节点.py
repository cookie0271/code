class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        depth = father = None
        def dfs(node: Optional[TreeNode], fa: Optional[TreeNode], d: int) -> bool:
            if node is None:
                return False
            if node.val == x or node.val == y:  # 找到 x 或 y
                nonlocal depth, father
                if depth:  # 之前已找到 x y 其中一个
                    return depth == d and father != fa
                depth, father = d, fa  # 之前没找到，记录信息
            return dfs(node.left, node, d + 1) or dfs(node.right, node, d + 1)
        return dfs(root, None, 1)

