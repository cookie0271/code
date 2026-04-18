class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        right = n - 1
        while right and arr[right - 1] <= arr[right]:
            right -= 1
        if right == 0:  # arr 已经是非递减数组
            return 0
        # 此时 arr[right-1] > arr[right]
        ans = right  # 删除 arr[:right]
        left = 0  # 枚举 left
        while left == 0 or arr[left - 1] <= arr[left]:
            while right < n and arr[right] < arr[left]:
                right += 1
            # 此时 arr[left] <= arr[right]，删除 arr[left+1:right]
            ans = min(ans, right - left - 1)
            left += 1
        return ans
