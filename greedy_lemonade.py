'''
link:https://leetcode.com/problems/lemonade-change
'''
class Solution(object):
    def lemonadeChange(self, bills):
        
        f=0
        te=0
        for i in range(len(bills)):
            cash=bills[i]
            
            if cash==5:f+=1
            elif cash==10: 
                f,te=f-1,te+1
            elif cash==20:
                if te>0:
                    f,te=f-1,te-1
                else:
                    f=f-3
            if f<0 or te<0:
                return False
        return True
                
            

