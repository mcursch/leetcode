# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # need to combine several problems into one: reverse list, merge list, and slow/fast traversal

        # account for empty list
        if not head:
            return
        # find the middle node
        # slow and fast pointer method
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse the second part of the list
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        #merge the two sorted lists
        # stop when second.next is null, this is fine becasue were merging the next vars in each time
        first, second = head, prev
        while second.next:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
