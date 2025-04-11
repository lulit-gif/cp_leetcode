class Solution:
    def containsDuplicate(self, nums: List[int]):
        hashset = set()

        for n in nums:
            for n in nums:
                if n in hashset:
                    return True
                hashset.add(n)
            return False
        

        