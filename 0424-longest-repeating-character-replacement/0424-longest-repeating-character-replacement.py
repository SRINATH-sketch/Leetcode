class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        dict={}
        ans=0

        for i in range(len(s)):
            if(s[i] not in dict):
                dict[s[i]]=0
            dict[s[i]]+=1
            window_size=i-left+1

            while(window_size-max(dict.values())>k):
                dict[s[left]]-=1
                if(dict[s[left]]==0):
                    del dict[s[left]]
                left+=1
                window_size=i-left+1
            ans=max(ans,window_size)
        return ans