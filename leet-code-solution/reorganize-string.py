class Solution:
    def reorganizeString(self, s: str) -> str:
       
        N = len(s)
        visited = {}    
        mp = Counter(s)

        pq = []
        for i in range(N) :
            val = s[i]
            if((val in mp) and ((val not in visited) or (visited[val] != 1))) :
                pq.append([mp[val], val])
            visited[val] = 1   
        pq.sort()
        pq.reverse()

      
        result = [0]*(N)    
        prev = [-1, -1]
        l = 0
        while pq:
            # print(pq)

           
            k = pq.pop(0)
            if l > len(result)-1:
                break
          
            result[l] = k[1]

          
            if prev[0]:

                pq.append(prev)
                pq.sort()
                pq.reverse()
            prev = [k[0] - 1, k[1]]
            l += 1
        result = [str(i) for i in result]
        if '-1' in result or '0' in result:
            return ""
        else:
            return "".join(result)