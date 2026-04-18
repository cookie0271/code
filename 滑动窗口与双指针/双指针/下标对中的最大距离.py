class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = i = 0
        for j, y in enumerate(nums2):
            while i < len(nums1) and nums1[i] > y:
                i += 1
            if i == len(nums1):
                break
            ans = max(ans, j - i)
        return ans

