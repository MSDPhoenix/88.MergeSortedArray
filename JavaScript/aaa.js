/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    var i = 0;
    while(i<m){
        while(nums2.length >0 && nums1[i]> nums2[0]){
            nums1.splice(i,0,nums2[0])
            nums2.shift()
            nums1.pop()
            m++
        }
        i++
    }
    x = nums2.length
    for(let i=0; i<x ;i++){
        nums1[nums1.length-i-1] = nums2.pop()
    }
}

var nums1 = [1,2,3,0,0,0];
var m = 3;
var nums2 = [2,5,6];
var n = 3;

merge(nums1,m,nums2,n)

console.log(nums1)




