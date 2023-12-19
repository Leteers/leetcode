class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string= s.split(' ')
        return(len(string))
s=Solution()
print(s.lengthOfLastWord("   fly me   to   the moon  "))