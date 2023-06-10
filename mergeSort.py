class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1 = nums1[:m]
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        print(nums1)
        
akua = Solution()
akua.merge([1,2,3,0,0,0],3,[2,5,6],3)
