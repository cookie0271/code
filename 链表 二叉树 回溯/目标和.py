class Solution:
    # 78. 子集（二进制枚举写法）
    def subsets(self, nums: List[int]) -> Dict[int, int]:
        cnt = defaultdict(int)
        for i in range(1 << len(nums)):
            s = sum(x for j, x in enumerate(nums) if i >> j & 1)
            cnt[s] += 1
        return cnt

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums) - abs(target)
        if s < 0 or s % 2:
            return 0

        m = s // 2
        k = len(nums) // 2
        cnt1 = self.subsets(nums[:k])
        cnt2 = self.subsets(nums[k:])

        return sum(c1 * cnt2[m - x] for x, c1 in cnt1.items())

