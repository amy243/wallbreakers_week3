'''
link:https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons
'''
class Solution(object):
    def findMinArrowShots(self, points):
        count=0
        points.sort(key=lambda x: x[-1])
        r=-float('inf')
        for i in points:
            if i[0]>r:

                count+=1
                r=i[1]

        return count

