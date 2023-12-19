class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters_count1 = {num: ransomNote.count(num) for num in set(ransomNote)}
        letters_count2= {num: magazine.count(num) for num in set(magazine)}
        for letter in letters_count1.keys():
            if letter in letters_count2.keys() and letters_count1[letter] <= letters_count2[letter]:
                pass
            else:
                return False
        return True

s = Solution()
ransomNote = "aa"
magazine = "aab"
print(s.canConstruct(ransomNote,magazine))