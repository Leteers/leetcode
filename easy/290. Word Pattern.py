import itertools
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        x = set(itertools.zip_longest(pattern,(s.split(' '))))
        print(x)
        return len(set(pattern))==len(set(s))==len(x)
pattern = "abba"
s = "dog cat cat dog"
sol = Solution()
print(sol.wordPattern(pattern, s))
