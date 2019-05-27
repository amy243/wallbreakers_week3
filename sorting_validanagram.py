'''
link:https://leetcode.com/problems/valid-anagram
'''

class Solution(object):
    def isAnagram(self, s, t):

        return (sorted(t)==sorted(s))
