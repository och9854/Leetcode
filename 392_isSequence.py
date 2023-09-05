# 1st submit
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ans = 0
        cnt = -1
        # loop len(t) times while ans == len(s) and cnt < len(t):
        while (ans != len(s) and cnt < len(t)-1):
            cnt += 1
            # if a char in t is equal to a char in s by order
            if s[ans] == t[cnt]:
                ans += 1
                continue
              
        return (ans == len(s))

# 2nd sumbit (improved)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for c in s:
            try:
                idx = t.index(c)
                t = t[idx+1:] 
            except:
                return False

        return True



# Answer was
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
'''

# Feedback
## need to make sure the index