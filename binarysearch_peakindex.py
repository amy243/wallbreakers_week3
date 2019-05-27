'''
link:https://leetcode.com/problems/peak-index-in-a-mountain-array
'''
class Solution(object):
    def peakIndexInMountainArray(self, A):

        sta = 0
        stp=len(A) - 1
        while sta < stp:
            mi = (sta + stp) // 2
            if A[mi] < A[mi + 1]:
                sta = mi + 1
            else:
                stp = mi
        return sta
        
