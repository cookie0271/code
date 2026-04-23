'''
题意
给你 n 个一样长的区间，每个区间选一个数，最大化得分。得分即所选数字中的任意两数之差的最小值。

二分答案
假设得分为 score。

把区间按照左端点排序。这样我们只需考虑相邻区间所选数字之差。

设从第一个区间选了数字 x，那么第二个区间所选的数字至少为 x+score，否则不满足得分的定义。

由于得分越大，所选数字越可能不在区间内，有单调性，可以二分答案。

或者说，看到「最大化最小值」就要先思考二分。

贪心
现在问题变成：

给定 score，能否从每个区间各选一个数，使得任意两数之差的最小值至少为 score。
⚠注意：这里是至少，不是恰好，两数之差的最小值可以不等于 score。由于二分会不断缩小范围，最终一定会缩小到任意两数之差的最小值恰好等于 score 的位置上。

把区间按照左端点排序。第一个数选谁？

贪心地想，第一个数越小，第二个数就越能在区间内，所以第一个数要选 x 
0
​
 =start[0]。

如果第二个数 x 
1
​
 =x 
0
​
 +score 超过了区间右端点 start[1]+d，那么 score 太大了，应当减小二分的右边界 right。

如果 x 
1
​
 ≤start[1]+d，我们还需要保证 x 
1
​
  大于等于区间左端点 start[1]，所以最终

x 
1
​
 =max(x 
0
​
 +score,start[1])
依此类推，第 i 个区间所选的数为

x 
i
​
 =max(x 
i−1
​
 +score,start[i])
必须满足

x 
i
​
 ≤start[i]+d
如果所有选的数都满足上式，那么增大二分的左边界 left。

细节
下面代码采用开区间二分，这仅仅是二分的一种写法，使用闭区间或者半闭半开区间都是可以的。

开区间左端点初始值：0。一定可以选出 n 个数，两两之差都大于等于 0。
开区间右端点初始值：⌊ 
n−1
start[n−1]+d−start[0]
​
 ⌋+1。最小值不会大于平均值，所以比平均值更大的数必然无法满足要求。
对于开区间写法，简单来说 check(mid) == true 时更新的是谁，最后就返回谁。相比其他二分写法，开区间写法不需要思考加一减一等细节，更简单。推荐使用开区间写二分。

代码实现时，可以假设第一个区间左边还选了一个数 −∞，这样不影响答案且代码更简洁。


'''
class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()

        def check(score: int) -> bool:
            x = -inf
            for s in start:
                x = max(x + score, s)  # x 必须 >= 区间左端点 s
                if x > s + d:
                    return False
            return True

        left, right = 0, (start[-1] + d - start[0]) // (len(start) - 1) + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left

