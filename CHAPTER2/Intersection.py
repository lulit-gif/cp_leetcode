class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i,j = 0,0
        output = []
        nums1,nums2 = sorted(nums1),sorted(nums2)
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                output.append(nums1[i])
                i+=1
                j+=1
        return output

        