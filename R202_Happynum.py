class Solution:
    def isHappy(self, n: int) -> bool:

        # if num is 1
        if n == 1:
            return True
            
        def next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n not in seen:
            seen.add(n)
            n = next(n)

        return n==1