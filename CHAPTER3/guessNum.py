# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
#we want to initialize the pointers based on full range of numbers

class Solution:
    def guessNumber(self, n: int):
        left = 1
        right = n

        while left<right:
            mid = (left+right)//2
            result = guess(mid)

            if result == 0:
                return mid
            if result == 1:
                left = mid + 1
            else :
                right = mid-1
        return left
                
        
    


        