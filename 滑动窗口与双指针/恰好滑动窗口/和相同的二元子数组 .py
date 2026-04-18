class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        l1 = l2= res=tmp_sum_1= tmp_sum_2=  0
        for r, num in enumerate(nums):
            tmp_sum_1 += num
            tmp_sum_2 += num

            #计算 sum >= k
            while l1 <= r and tmp_sum_1 >= goal:
                tmp_sum_1 -= nums[l1]
                l1+=1

            #计算 sum >= k+1
            while l2 <= r and tmp_sum_2 >= goal+1:
                tmp_sum_2 -= nums[l2]
                l2+=1
            # count(sum==k)= count(sum>=k+1) - count(sum>=k)
            res += (l1-l2)
        return res

