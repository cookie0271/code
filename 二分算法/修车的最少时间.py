'''
请注意，能力值越低，修车越快。（按照英文描述，ranks 
i
​
  应该翻译成「排名」，排名越靠前，修车越快。）

如果已知修车的时间 t，我们可以算出每个人在 t 分钟内能修好多少辆车。例如一个能力值 r=3 的人可以在 t=16 分钟内修好 2 辆车，但无法修好 3 辆车。

根据题意，需要满足

rn^2≤t
上式表明，t 越大，能修的车越多，越能满足要求。有了这样的单调性，我们就可以二分答案了。

二分上界为 min(ranks)⋅cars 
2
 ，即让能力值最低（修车最快）的人修好所有车所需要的时间。

'''
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 0
        right = min(ranks) * cars * cars
        while left + 1 < right:  # 开区间
            mid = (left + right) // 2
            if sum(isqrt(mid // r) for r in ranks) >= cars:
                right = mid  # 满足要求
            else:
                left = mid
        return right  # 最小的满足要求的值

