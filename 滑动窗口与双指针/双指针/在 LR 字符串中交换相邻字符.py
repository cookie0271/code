class Solution:
    def canTransform(self, start: str, target: str) -> bool:
        if start.replace('X', '') != target.replace('X', ''):
            return False
        j = 0
        for i, c in enumerate(start):
            if c == 'X':
                continue
            while target[j] == 'X':
                j += 1
            if i != j and (c == 'L') != (i > j):
                return False
            j += 1
        return True

