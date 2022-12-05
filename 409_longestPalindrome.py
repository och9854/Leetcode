class Solution:
    def longestPalindrome(self, s):
        ans = 0
        a = collections.Counter(s).values()
        
        for v in a:
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans