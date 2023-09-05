# my answer
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #init
        ans = dict()

        for num in nums:
            # if num is already in dictionary
            if num in ans:
                return True
            # else: add it
            else:
                ans[num] = 1




            
        return False
    

# solution