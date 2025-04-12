class Solution:
    def twoSum(self, nums: List[int], target: int) ->
        num_dict ={}

        for i,num in enumerate(nums):
            indx = target - num

            if indx in num_dict:
                return [num_dict[indx],i]

            num_dict[num] = i

        return []

        
        
