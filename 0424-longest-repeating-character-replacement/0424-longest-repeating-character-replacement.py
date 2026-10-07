class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        freq={}
        ans=0
        
        for i in range(len(s)):
            if(s[i] not in freq):
                freq[s[i]]=0
            freq[s[i]]+=1
            window_size=i-left+1
            
            while(window_size-max(freq.values())>k):
                freq[s[left]]-=1
                if(freq[s[left]]==0):
                    del freq[s[left]]
                left+=1
                window_size=i-left+1
            ans=max(ans,window_size)
        return ans