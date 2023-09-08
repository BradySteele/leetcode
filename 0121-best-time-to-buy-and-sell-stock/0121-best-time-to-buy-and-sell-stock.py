class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
        
        max_profit = 0
        min_price = prices[0]
        
        for i in prices[1:]:
            max_profit = max(max_profit, i - min_price)
            min_price = min(min_price, i)
            
        return max_profit