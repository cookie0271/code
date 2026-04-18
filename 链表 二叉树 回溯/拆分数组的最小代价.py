class Solution:
    def closeLampInTree(self, root: TreeNode) -> int:
        @cache  # 记忆化搜索
        def dfs(node: TreeNode, switch2: bool, switch3: bool) -> int:
            if node is None:
                return 0
            if (node.val == 1) == (switch2 == switch3):  # 当前节点为开灯
                res1 = dfs(node.left, switch2, False) + dfs(node.right, switch2, False) + 1
                res2 = dfs(node.left, not switch2, False) + dfs(node.right, not switch2, False) + 1
                res3 = dfs(node.left, switch2, True) + dfs(node.right, switch2, True) + 1
                res123 = dfs(node.left, not switch2, True) + dfs(node.right, not switch2, True) + 3
                return min(res1, res2, res3, res123)
            else:  # 当前节点为关灯
                res0 = dfs(node.left, switch2, False) + dfs(node.right, switch2, False)
                res12 = dfs(node.left, not switch2, False) + dfs(node.right, not switch2, False) + 2
                res13 = dfs(node.left, switch2, True) + dfs(node.right, switch2, True) + 2
                res23 = dfs(node.left, not switch2, True) + dfs(node.right, not switch2, True) + 2
                return min(res0, res12, res13, res23)
        return dfs(root, False, False)
