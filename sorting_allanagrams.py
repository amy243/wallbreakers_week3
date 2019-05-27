'''
link: https://leetcode.com/problems/find-all-anagrams-in-a-string
'''
class Solution(object):
    def findAnagrams(self, s, p):


        word=[]
        p=''.join(sorted(p))

        for i in range(len(s)-len(p)+1):
            if s[i] in p:
                new=''.join(sorted(s[i:i+len(p)]))
                if new==p:
                    word.append(i)
        return word
