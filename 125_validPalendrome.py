class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = [val for val in s if val.isalnum()]
        string = ''.join(string).lower().replace(" ","")
        
        left = 0
        right = len(string) - 1
        flag = False

        # edge case
        if right <= 0:
            return True

        # general case
        while left < right:
            if string[left] == string[right]:
                # shift
                left += 1
                right -= 1
                flag = True
                pass
            else:
                return False
        
        
        return flag
        
# Answer
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:

        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True

'''

# Feedback
'''
check isalnum WITH moving two pointers
'''

            
