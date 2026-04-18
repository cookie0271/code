class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        vis = {tuple(nums1)}
        q = [nums1]
        for ans in count(0):
            tmp = q
            q = []
            for a in tmp:
                if a == nums2:
                    return ans
                for l in range(n):
                    for r in range(l + 1, n + 1):
                        sub = a[l: r]
                        b = a[:l] + a[r:]  # 从 a 中移除 sub
                        for i in range(len(b) + 1):
                            c = b[:i] + sub + b[i:]
                            t = tuple(c)
                            if t not in vis:
                                vis.add(t)
                                q.append(c)

