class Solution(object):
    def merge(self, nums1, m, nums2, n):

        if n == 0:return
        len1 = len(nums1)
        end_idx = len1-1

        while n > 0 and m > 0:
            if nums2[n-1] >= nums1[m-1]:
                nums1[end_idx] = nums2[n-1]
                n-=1
            
            else:
                nums1[end_idx] = nums1[m-1]
                m-=1
            end_idx-=1

        while n > 0:
            nums1[end_idx] = nums2[n-1]
            n-=1
            end_idx-=1



        

        