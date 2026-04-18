def f(a: List[int]) -> None:
    for i, x in enumerate(a):
        if x % 2: a[i] = -x  # 由于元素都是正数，把奇数变成相反数，这样排序后奇偶就自动分开了
    a.sort()

class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        f(nums)
        f(target)
        return sum(abs(x - y) for x, y in zip(nums, target)) // 4

