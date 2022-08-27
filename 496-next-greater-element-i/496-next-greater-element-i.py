class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        new_arr = []
        
        for i in range(len(nums1)):
            flag = False
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    flag = True 
                elif flag and nums1[i] < nums2[j]:
                    new_arr.append(nums2[j])
                    flag = False
            if flag:
                new_arr.append(-1)
                        
                   
        return new_arr
                    
        