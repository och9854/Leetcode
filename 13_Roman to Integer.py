# mine
class Solution:
    def romanToInt(self, s: str) -> int:
        #init
        nums = {'I': 1, "V": 5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        specNums = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        res = 0
        
        # 2char: sum, remove specNums
        for i, j in specNums.items():
            if i in s:
                res += j * s.count(i)
                s = s.replace(i, "")
            

        # 1char: sum all
        for i, j in nums.items():
            if i in s:
                res += j * s.count(i)
                s = s.replace(i, "")

        return res

# Answer
