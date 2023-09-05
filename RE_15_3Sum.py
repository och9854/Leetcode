class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #init
        res = []
        nums.sort()

        #loop the List
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSumII(nums, i , res)
        return res
    
    
    def twoSumII(self, nums: List[int], i:int, res: List[List[int]]):
        lo, hi = i+1, len(nums)-1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum<0:
                lo +=1 
            elif sum>0:
                hi -= 1
            else:
                res.append([ nums[i], nums[lo], nums[hi] ])
                lo += 1
                hi -= 1
                # skip same value
                while lo < hi and nums[lo] == nums[lo- 1]:
                    lo += 1
'''Feedback

- Didn't check the duplicates at first. 




'''