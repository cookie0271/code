def count_vowel(s: str) -> int:
    return sum(c in "aeiou" for c in s)

class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        cnt0 = count_vowel(a[0])
        for i in range(1, len(a)):
            if count_vowel(a[i]) == cnt0:
                a[i] = a[i][::-1]
        return ' '.join(a)

