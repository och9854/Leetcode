class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        result = 1


        while (left <= right):
            mid = (left + right) // 2
            
            if (isBadVersion(mid)):
                right=mid - 1
                result = mid
            else:
                left = mid + 1

            
        return int(left)