class Solution:
    def connect(self, root: 'Node') -> 'Node':
        pre = []
        def dfs(node: 'Node', depth: int) -> None:
            if node is None:
                return
            if depth == len(pre):  # node 是这一层最左边的节点
                pre.append(node)
            else:  # pre[depth] 是 node 左边的节点
                pre[depth].next = node  # node 左边的节点指向 node
                pre[depth] = node
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 0)  # 根节点的深度为 0
        return root

#或者
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        q = [root]
        while q:
            # 从左到右依次连接
            for x, y in pairwise(q):
                x.next = y
            # 准备下一层的节点
            tmp = q
            q = []
            for node in tmp:
                if node.left:  q.append(node.left)
                if node.right: q.append(node.right)
        return root

# 或者
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur = root
        while cur:
            nxt = dummy = Node()  # 下一层的链表
            while cur:  # 遍历当前层的链表
                if cur.left:
                    nxt.next = cur.left  # 下一层的相邻节点连起来
                    nxt = cur.left
                if cur.right:
                    nxt.next = cur.right  # 下一层的相邻节点连起来
                    nxt = cur.right
                cur = cur.next  # 当前层链表的下一个节点
            cur = dummy.next  # 下一层链表的头节点
        return root

