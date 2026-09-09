# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current=head
        count=0
        while(current):
            count+=1
            current=current.next
        pos=count-n

        if(pos==0):
            return head.next

        k=0
        prev=None
        curr=head
        while(curr):
            if(k==pos):
                prev.next=curr.next
                break
            k+=1
            prev=curr
            curr=curr.next
        return head