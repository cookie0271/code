class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        def dfs(node: 'Node') -> None:
            if node is None:
                return
            for c in node.children:
                dfs(c)
            ans.append(node.val)
        dfs(root)
        return ans
