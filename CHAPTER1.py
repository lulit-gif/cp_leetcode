class Solution:
    def addDigits(self, num: int):
        while num>9:
            digit = 0
            while num:
                digit +=(num%10)
                num//=10
            num = digit

        return num

        
