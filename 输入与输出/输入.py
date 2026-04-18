# 输入
# 选择1
import sys
data = list(map(int,sys.stdin.read().split))
if not data:
    print("false") #print("error")
    exit(0)
index = 0
n = data[index]
index += 1
#后续就是用index给变量赋值
#如果是数组 那就是 for i in range(n):  nums[0]=data[index]  index+=1
#如果是链表 那就是 head = Listcode(data[index]) index += 1 cur=head for i in range (1,n): node = ListNode(data[index]) cor.next = node cur = node index+=1
#如果是数 那就分完全二叉树和非完全二叉树

# 递归构建完全二叉树
def build_tree(nums, idx):
    n = len(nums)
    # 若下标越界，该位置没有节点
    if idx >= n:
        return None
    # 创建当前节点
    node = Node(nums[idx])
    # 递归构建左子树和右子树
    node.left = build_tree(nums, 2 * idx + 1)
    node.right = build_tree(nums, 2 * idx + 2)
    return node

# 递归 DFS 收集叶子节点
def collect_leaves(root, leaves):
    if root is None:
        return
    # 若没有左右孩子，则为叶子节点
    if root.left is None and root.right is None:
        leaves.append(root.val)
        return
    # 否则继续递归左右子树
    collect_leaves(root.left, leaves)
    collect_leaves(root.right, leaves)



#对于普通二叉树
def build_tree(nums):
    n = len(nums)
    if n == 0 or nums[0] == -1:
        return None

    # nodes[i] 对应 nums[i] 的节点引用
    nodes = [None] * n
    nodes[0] = Node(nums[0])

    for i in range(1, n):
        if nums[i] == -1:
            continue
        p = (i - 1) // 2
        if p >= 0 and nodes[p] is not None:
            nodes[i] = Node(nums[i])
            if i == 2 * p + 1:
                nodes[p].left = nodes[i]
            else:
                nodes[p].right = nodes[i]
    return nodes[0]

def bfs(root):
    if not root:
        return
    q = deque([root])
    while q:
        cur = q.popleft()
        print(cur.val)
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
