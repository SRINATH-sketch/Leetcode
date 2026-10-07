class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        left=0
        right=len(people)-1
        boat=0
        people.sort()
        while(left<=right):
            if(people[right]+people[left]<=limit):
                left+=1
                right-=1
                boat+=1
            else:
                right-=1
                boat+=1
        return boat