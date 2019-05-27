'''
link:https://leetcode.com/problems/binary-search
'''
class Solution(object):
    def search(self, nums, target):

        l=0
        r=len(nums)-1
        #def re(l,r):
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                return m
            else:
                if target<nums[m]:
                    r=m-1
                else:

                    l=m+1

        return -1

        
