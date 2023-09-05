'''
- "i"th day prices
- P: maximize profit = low price, high price
# Solution
1. 매수가 체크
    매수가가 낮으면 변경
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0] # 매수가
        for i in prices:
            if buy > i: # 매수가가 더 낮으면
                buy = i # 매수가 변경
            # 둘중 뭐가 이득인지 
            profit = max(i-buy, profit) 
        return profit
