WIDTH = 15  # nums[i] 二进制长度的最大值


class Node:
    __slots__ = 'son', 'leaf'

    def __init__(self):
        self.son = [None] * 2
        self.leaf = 0  # 子树叶子个数


class Trie:
    def __init__(self):
        self.root = Node()

    def put(self, val: int) -> Node:
        cur = self.root
        for i in range(WIDTH - 1, -1, -1):
            bit = val >> i & 1
            if cur.son[bit] is None:
                cur.son[bit] = Node()
            cur = cur.son[bit]
            cur.leaf += 1

    def delete(self, val: int) -> Node:
        cur = self.root
        for i in range(WIDTH - 1, -1, -1):
            cur = cur.son[val >> i & 1]
            cur.leaf -= 1  # 如果减成 0 了，说明子树是空的，可以理解成 cur is None

    def max_xor(self, val: int) -> int:
        cur = self.root
        ans = 0
        for i in range(WIDTH - 1, -1, -1):
            bit = val >> i & 1
            if cur.son[bit ^ 1] and cur.son[bit ^ 1].leaf:
                ans |= 1 << i
                bit ^= 1
            cur = cur.son[bit]
        return ans


class Solution:
    def maxXor(self, nums: list[int], k: int) -> int:
        pre = list(accumulate(nums, xor, initial=0))

        t = Trie()
        min_q = deque()
        max_q = deque()
        ans = left = 0
        for right, x in enumerate(nums):
            # 1. 入
            t.put(pre[right])

            while min_q and x <= nums[min_q[-1]]:
                min_q.pop()
            min_q.append(right)

            while max_q and x >= nums[max_q[-1]]:
                max_q.pop()
            max_q.append(right)

            # 2. 出
            while nums[max_q[0]] - nums[min_q[0]] > k:
                t.delete(pre[left])
                left += 1
                if min_q[0] < left:
                    min_q.popleft()
                if max_q[0] < left:
                    max_q.popleft()

            # 3. 更新答案
            ans = max(ans, t.max_xor(pre[right + 1]))
        return ans

