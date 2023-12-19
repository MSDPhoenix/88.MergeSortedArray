class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()

    # iterate throught the xeros at the end of num one
    # start at index m and end at index m+n
    # for each index, replace zero with the corresponding value from nums2
    # use built-in method to sort nums1 sequentially

