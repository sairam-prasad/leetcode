class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        temp,rev = x,0
        
        while x>0:
            rev=(rev*10)+(x%10)
            x=x//10
            print(rev)
        
        print(rev)
        if rev==temp:
            return True
        return False
    