# Could not solve


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: 
            return 0
        left = ans = 0
        curr = 1
        # iterate right for len(nums)
        for right in range(len(nums)):
            curr *= nums[right]
            
            while curr >= k:
                curr /= nums[left]
                left += 1
            
            ans += (right) * (right+1) / 2 

        return int(ans)
            

# answer

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod //= nums[left]
                left += 1
            ans += right - left + 1
        return ans


# feedback
## PROBLEM: missed how the outputs come out(line 18, 35)
## NEXT TIME: write down the outputs one by one