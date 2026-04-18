class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = None
        max_depth = -1  # 全局最大深度
        def dfs(node: Optional[TreeNode], depth: int) -> int:
            nonlocal ans, max_depth
            if node is None:
                max_depth = max(max_depth, depth)  # 维护全局最大深度
                return depth
            left_max_depth = dfs(node.left, depth + 1)  # 左子树最深空节点的深度
            right_max_depth = dfs(node.right, depth + 1)  # 右子树最深空节点的深度
            if left_max_depth == right_max_depth == max_depth:  # 最深的空节点左右子树都有
                ans = node  # 如果后面发现了更大的 max_depth，答案还会更新
            return max(left_max_depth, right_max_depth)  # 当前子树最深空节点的深度
        dfs(root, 0)
        return ans
