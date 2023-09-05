class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        two pointer -> sum from both side
        '''
        res = -1
        right_sum = sum(nums) - nums[0]
        left_sum = 0
        idx = 0

        # edge from left
        if right_sum == left_sum:
            return 0

        # iter
        while idx < len(nums)-1:

            print(f"{ idx, left_sum, right_sum}")
            if right_sum == left_sum:
                return idx
            else:
                left_sum += nums[idx]
                idx += 1
                right_sum -= nums[idx]

        # last edge
        if right_sum == left_sum:
            return idx

        return -1
            
