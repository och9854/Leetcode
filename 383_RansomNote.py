class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ran = {i: ransomNote.count(i) for i in set(ransomNote)}
        mag = {j: magazine.count(j) for j in set(magazine)}
        
        for k in ransomNote:
            if k not in mag.keys():
                return False
            elif ran[k] > mag[k]:
                return False
        
        return True
        