class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if(x < 0):
            return False
        
        cnv_str = str(x)
        reverse_x = int(cnv_str[::-1])
        if(x == reverse_x):
            return True
        else:
            return False
        