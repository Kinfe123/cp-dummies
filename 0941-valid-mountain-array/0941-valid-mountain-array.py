class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return False
        else:
            max_ = max(arr)
            max_index = arr.index(max_)
            first_one = arr[:max_index+1]
            second_one = arr[max_index:]
            state = False

            print(second_one)
            if len(set(first_one)) == len(first_one) and len(set(second_one)) == len(second_one) and len(second_one) >= 2 and len(first_one) >=2 :
                sorted_one = sorted(first_one)
                sorted_two = sorted(second_one , reverse=True)
                
                if sorted_one == first_one and second_one == sorted_two:
                    state = True
                else:
                    state = False
            return state
