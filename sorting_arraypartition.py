'''
link:https://leetcode.com/problems/array-partition-i
'''
class Solution(object):
    def arrayPairSum(self, nums):

        return sum(sorted(nums)[::2])
