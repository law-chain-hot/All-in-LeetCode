# 121. Best Time to Buy and Sell Stock

"""
# { 2020.05.14 } 
# { Method 1: Record all 0 and del them later }
# { Optimal: Method 1 }
    - Time complexity:   O(n)!
    - Space complexity:  O(n) 

# { My own explanation of this problem }


Can I think of it along the way


"""



class Solution:
    def maxProfit(self, prices: List[int]):
        min_price, max_profit  = float('inf'), 0
        for price in prices:    
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


