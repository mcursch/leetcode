# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we will be reversing the list, by going through one node at a time,
        #and makeing them point the opposite way
        #need a previous node to point back to, and a current node to work with
        #set previous to None, because the tail must point to nothing (in first iteration)
        prev, cur = None, head

        #while the current node is not null, this will get us to the tail
        while cur:
            # were going to break the connection between cur node and its next one, so save that in a temp
            temp = cur.next
            # break connection by pointing cur to the node before it (or in the first iteration, Null)
            cur.next = prev
            # this node is reversed, so now we need to iterate. First, set the current node as the prev for the next iteration
            prev = cur
            # now, update cur to the next value, which we stored in temp
            cur = temp
        #once the iterations are done, prev will be set to our current node, which will be the head of the new list
        return prev
