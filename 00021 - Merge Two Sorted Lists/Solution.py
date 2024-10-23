# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy node to track the start of our new ordered list
        # node to use as tracker for the list, so set them equal in the beginning
        dummy = node = ListNode()
        # perform this loop until one (or both) of the lists runs out
        while list1 and list2:
            # if the value of list1 is less than list2, point our current combo array to it, and increment the list
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            # if the value of list2 is less than list2, point our current combo array to it, and increment the list
            else:
                node.next = list2
                list2 = list2.next
            # increment the combo array to the value we just added
            node = node.next

        # lists might not be equal length, so if one runs out, append the rest of the other one to the list
        # this only works because the lists are in ascending order, so the list with the highest vals will always be the last one
        node.next = list1 or list2

        # dummy.next points to the start of our list, so return it
        return dummy.next




