class Solution:
    def countOdds(self, low: int, high: int):
    #output should be int
        length = high -low + 1
        count = length //2
        if length %2 and low %2:
            count += 1
        else:
             return count