class Solution:
    def reverse(self, x: int):
        is_negative = x < 0
        x = abs(x)

        reversed_num = 0
        while x >0 :
            reversed_num = reversed_num*10 +x%10
            x//= 10

        if is_negative:
            reversed_num = -reversed_num
        #If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
        if reversed_num < -2**31 or reversed_num > 2**31:
            return 0
        
        return reversed_num
        
        