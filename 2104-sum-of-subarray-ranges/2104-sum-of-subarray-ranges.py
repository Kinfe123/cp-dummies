class Solution():
    
    def subArrayRanges(self, nums: List[int]) -> int:

            n = len(nums)
            #first calculate the max values

            #using monotonic stack
            stack = [] 

            dp_incr = [0]*n
            for j in range(n):
                num = nums[j]

                while stack and stack[-1][1]<=num: stack.pop() #small number not helpful, since we are only interested in big numbers

                if stack:
                    dp_incr[j]= num*(j-stack[-1][0]) + dp_incr[stack[-1][0]]

                else: dp_incr[j]= num*(j+1)

                #update the stack
                stack.append((j,num))


            #now min values
            stack = []
            dp_decr =[0]*n
            for j in range(n):
                num= nums[j]

                while stack and stack[-1][1]>=num: stack.pop() #safe, big number not helpful

                if stack:
                    dp_decr[j] = num*(j-stack[-1][0]) + dp_decr[stack[-1][0]]

                else: dp_decr[j] = num*(j+1)

                #update the stack
                stack.append((j,num))


            ans = 0
            for j in range(n):
                ans += dp_incr[j]-dp_decr[j]

            return ans