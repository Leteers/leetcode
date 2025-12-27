class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2:
            arr = []
            numbers = list(map(int,[*s]))
            for i in range(len(numbers)-1):
                arr.append((numbers[i]+numbers[i+1])%10)
            s = ''.join(list(map(str,arr)) )
            del arr
        if s[0] == s[1]:
            return True
        else:
            return False
 
sol = Solution()
print(sol.hasSameDigits("34789"))