class Solution(object):
    def merge(self, nums1, m, nums2, n):
        
        i1,i2,iw = m-1,n-1,len(nums1)-1

        while i2 >=0:
            if i1 >= 0 and nums1[i1] > nums2[i2]:
                nums1[iw] = nums1[i1]
                i1 -= 1
            else:
                nums1[iw] = nums2[i2]
                i2 -= 1
            iw -= 1


# iterate through the nums1 backwards
# define the index_a to begin iteratiing thought nums1 
# define the index_b to begin iteratiing thought nums2
# define index to write a new value to
# while index_b is not_0
    # if index_a is not below zero, and the value of that index is greater than the last value of nums2
        # replace the value at index_to_write_to with the value at index_a
    # if index_a is below zero or the value in nums1 at index_a is not greater than the last value of nums2
        # replace the value at index_to_write_to with the value at index_b
    # decrement index_to_write_to

