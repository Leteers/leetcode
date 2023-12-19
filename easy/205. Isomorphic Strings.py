class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a=[]
        if len(s) == len(t):
            for i in range(len(s)):
                a.append((s[i],t[i]))
        return len(set(a)) == len(set(s)) == len(set(t))


s = "paper"
t = "title"

sol= Solution()
print(sol.isIsomorphic(s,t))