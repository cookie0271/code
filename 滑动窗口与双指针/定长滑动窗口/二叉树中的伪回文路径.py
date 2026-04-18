class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        p = [0] * 10

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            p[node.val] ^= 1  # 修改 node.val 出现次数的奇偶性
            if node.left is None and node.right is None:  # node 是叶子节点
                res = 1 if sum(p) <= 1 else 0
            else:
                res = dfs(node.left) + dfs(node.right)
            # 恢复到递归 node 之前的状态（不做这一步就把 node.val 算到其它路径中了）
            p[node.val] ^= 1
            return res

        return dfs(root)

