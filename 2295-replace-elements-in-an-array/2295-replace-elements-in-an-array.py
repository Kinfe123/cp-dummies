class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hash_dict = {}
        for i in range(0 , len(nums)):
            hash_dict[nums[i]] = i

      

        for i in operations:
            element = i[0]
            new_element = i[1]
            hash_dict[new_element] = hash_dict[element]
            hash_dict.pop(element)

        ans = [0]*len(nums)
        

        for keys , values in hash_dict.items():
           
            ans[values] = keys

        return ans
