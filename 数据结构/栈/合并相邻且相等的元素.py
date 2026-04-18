class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        st = []
        for x in nums:
            st.append(x)
            while len(st) > 1 and st[-1] == st[-2]:
                st.pop()
                st[-1] *= 2
        return st

