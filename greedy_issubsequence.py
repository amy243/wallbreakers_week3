'''
link: https://leetcode.com/problems/is-subsequence
'''
class Solution(object):
    def isSubsequence(self,s,t):
        if len(s)==0:
            return True
        if len(t)==0:
            return False
        i,j=0,0
        while j < (len(s)) and i < len(t):

            if s[j]==t[i]:
                j+=1
            i+=1
        if j==len(s):
            return True
        else:
            return False
