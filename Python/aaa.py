class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        while i < m:
            while len(nums2) > 0 and nums1[i] > nums2[0] :
                nums1.insert(i,nums2[0])
                nums2 = nums2[1:]
                nums1.pop()
                m += 1
            i += 1
        for i in range(len(nums2)):
            nums1[-i-1] = nums2.pop()


# iterate through nums 1
        # compare current value in nums one with first value of nums 2
        # while nums2 is not empty and nums1 current value is greater than nums2 first value:
            # insert nums2 value at current index of nums1
            # remove first value from nums2
            # remove a zero from the end of nums1

        # while the current value in nums 1 is less than the first value in nums 2