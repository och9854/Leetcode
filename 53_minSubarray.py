class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # init
        current_sub = max_sub = nums[0]
        
        # loop
        for n in nums[1:]:
            current_sub = max(current_sub + n, n)
            max_sub = max(current_sub, max_sub)
            
        return max_sub
        