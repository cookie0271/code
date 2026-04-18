class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        s = 0
        def dfs(node: TreeNode) -> None:
            if node is None:
                return
            dfs(node.right)  # 递归右子树
            # 递归结束后，s 就等于右子树的所有节点值之和
            nonlocal s
            s += node.val
            node.val = s  # 此时 s 就是 >= node.val 的所有数之和
            dfs(node.left)  # 递归左子树
        dfs(root)
        return root

