class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pro = 0
        minprice = prices[0]
        for price in prices:
            minprice = min(minprice,price)
            pro = max(pro,price-minprice)
        return pro