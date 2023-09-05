# 347. Top K Frequent Elements

from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = Counter(nums)

        answer = []
        for i in count_dict.most_common(k):
            answer.append(i[0])

        return answer
