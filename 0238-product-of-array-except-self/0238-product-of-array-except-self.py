class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_product = []
        post_product = []
        #two pass to build the prefix product of the lists 
        pro_ = 1 
        for i in range(len(nums)):
            pre_product.append(pro_)
            pro_*=nums[i]
        
        pro_ = 1
        for i in range(len(nums)-1 , -1,-1):
            post_product.append(pro_)
            pro_*=nums[i]
        post_product.reverse()
        
        for i in range(len(nums)):
            pre_product[i] = pre_product[i] * post_product[i]
        return pre_product
        