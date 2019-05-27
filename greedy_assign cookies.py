'''
link:https://leetcode.com/problems/assign-cookies
'''
class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        j=n=0

        for i in g:
            while j < len(s) and s[j] < i:
                j += 1
            if j != len(s):
                n += 1
                j += 1
            else:
                break
        return(n)


       
