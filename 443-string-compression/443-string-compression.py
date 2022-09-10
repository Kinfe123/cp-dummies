class Solution:
    def compress(self, array: List[str]) -> int:
        ans=[]
        i=0
        while i < len(array):
            temp=array[i]
            count=i+1
            while count<len(array)and array[count]==temp:
                count+=1
                if count==len(array):
                    break
            ans.append(temp)
            if count-i>1 and count-i<10:
                ans.append(str(count-i))
            if count-i>9:
                num=count-i
                dup=[]
                while num:
                    dup.append(str(num%10))
                    num//=10
                for j in range(len(dup)-1,-1,-1):
                    ans.append(dup[j])
            i=count
        array.clear()
        for i in range(len(ans)):
            array.append(ans[i])
        return len(ans)