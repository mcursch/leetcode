class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # tortoise and hair solution.
        # establish two pointers, both at the head
        # one moves twice as fast as the other
        # if they are ever equal, you have a cycle

        # establish two pointers, both at the head
        slow, fast = head, head

        while fast and fast.next:
            # one moves twice as fast as the other
            slow = slow.next
            fast = fast.next.next
            # if they are ever equal, you have a cycle
            if slow == fast:
                return True
        return False

