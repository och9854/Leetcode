# link: https://leetcode.com/problems/longest-consecutive-sequence/description/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        count = 0

        for x in num_set:  # 0
            if x-1 not in num_set:
                y = x+1  # 1 2 3 4
                # traverse to the end
                while y in num_set:
                    y += 1
                # re-max it
                count = max(count, y-x)

        return count
