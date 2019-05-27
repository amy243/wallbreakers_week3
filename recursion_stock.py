'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock
'''
class Solution(object):
    def maxProfit(self, prices):
        maxx, minn = 0, float('inf')
        for i in prices:
            minn = min(minn, i)
            profit = i - minn
            maxx = max(maxx, profit)
        return maxx
