class Solution:
    def reverse(self, x: int) -> int:
        reversed_num=0
        sign= 1 if x>0 else -1
        x=abs(x)
        while x>0:
            digit=x%10
            reversed_num=reversed_num*10+ digit
            x=x//10
        
        reversed_num*=sign
        return 0 if reversed_num>2**31 - 1 or reversed_num<-2**31 else reversed_num
