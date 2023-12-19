class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()

# replace the zeros in nums 1 with the values of nums2 using list indexing 
# use Python list method to sort them in sequential order.