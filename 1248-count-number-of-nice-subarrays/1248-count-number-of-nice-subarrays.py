class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        # countforsub  , l  , oddc , answer = 0  , 0 , 0 , 0
        # for r in range(len(nums)):
        #     if nums[r] % 2:
        #         oddc+=1
        #         countforsub=0
        #     while oddc == k:
        #         if nums[l] % 2:
        #             oddc-=1
        #             l+=1
        #         countforsub+=1
        #     answer+=countforsub
        # return answer
        count = 0
        curr_sum = 0
        map_ = {}
        for i in range(len(nums)):
            if nums[i]%2:
                nums[i] = 1
            else:
                nums[i] = 0
        for i in range(len(nums)):
            curr_sum+=nums[i]
            if curr_sum == k:
                count+=1
            if curr_sum - k in map_:
                count+=map_[curr_sum - k]
            if curr_sum in map_:
                map_[curr_sum] += 1
            else:
                map_[curr_sum] = 1
        return count

                