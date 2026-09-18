class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # arr=[]
        # for i in range(len(s)):
        #     if(s.count(s[i])==1):
        #         arr.append(s[i])
        #     elif(s.count(s[i])>1):
        #         arr.append(s[i])
        #         s.remove(s[i])
        # return len(arr)
        sets=set()
        i=0
        j=0
        c=0
        m=0
        while(j<len(s)):
            if(s[j] not in sets):
                sets.add(s[j])
                c+=1
                j+=1
                if(c>m):
                    m=c
            else:
                c-=1
                sets.remove(s[i])
                i+=1
        return m