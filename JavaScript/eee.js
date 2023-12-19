/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    for(let i = 0; i<m;i++){
            while(nums2.length >0 && nums1[i]> nums2[0]){
                nums1.splice(i,0,nums2[0]);
                nums2.shift();
                nums1.pop();
                m++;
            }
        }
        x = nums2.length;
        for(let i=0; i<x ;i++){
            nums1[nums1.length-i-1] = nums2.pop();
        }    
    
    }
