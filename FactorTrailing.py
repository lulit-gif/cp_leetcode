class Solution:
    def trailingZeroes(self, n: int):
         count=0
         while(n!=0):
            num = n//5
            count +=num
            n=num
         return count

        