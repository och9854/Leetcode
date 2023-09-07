# 238. Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0 for i in range(len(nums))]
        count_zero = nums.count(0)
        product = 1

        # more than two zeros
        if count_zero >= 2:
            return answer

        # one 0 in List
        if count_zero == 1:
            # find the multiple
            for num in nums:
                if num == 0:
                    pass
                else:
                    product *= num
            # fill it
            for idx, num in enumerate(nums):
                if num != 0:
                    pass
                else:
                    answer[idx] = product
            # return
            return answer

        # no 0 in List
        # get multiple
        for num in nums:
            product *= num

        # fill answerlist
        for idx, num in enumerate(nums):
            answer[idx] = int(product/num)
        return answer
