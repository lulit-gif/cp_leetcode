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
        
        return reversed_num
        