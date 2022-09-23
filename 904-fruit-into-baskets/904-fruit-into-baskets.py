class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window_start = 0
        number_freq = {}
        max_lenght = 0
        
        for window_end in range(len(fruits)):
            current = fruits[window_end]
            if current not in number_freq:
                number_freq[current] = 0
            number_freq[current]+=1
            
            while len(number_freq) > 2:
                left = fruits[window_start]
                number_freq[left]-=1
                if number_freq[left] == 0:
                    del number_freq[left]
                window_start+=1
                
            max_lenght = max(window_end - window_start +1 , max_lenght )
        return max_lenght