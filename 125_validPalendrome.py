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
        
            