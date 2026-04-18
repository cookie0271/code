class Node:
    __slots__ = 'son', 'min_l', 'i'

    def __init__(self):
        self.son = [None] * 26
        self.min_l = inf

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        ord_a = ord('a')
        root = Node()
        for idx, s in enumerate(wordsContainer):
            l = len(s)
            cur = root
            if l < cur.min_l:
                cur.min_l, cur.i = l, idx
            for c in map(ord, reversed(s)):
                c -= ord_a
                if cur.son[c] is None:
                    cur.son[c] = Node()
                cur = cur.son[c]
                if l < cur.min_l:
                    cur.min_l, cur.i = l, idx

        ans = []
        for s in wordsQuery:
            cur = root
            for c in map(ord, reversed(s)):
                c -= ord_a
                if cur.son[c] is None:
                    break
                cur = cur.son[c]
            ans.append(cur.i)
        return ans

