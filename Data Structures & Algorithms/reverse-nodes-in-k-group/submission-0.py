from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(
        self,
        head: Optional[ListNode],
        k: int
    ) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        group_previous = dummy

        while True:
            # Find the final node of the next group of k nodes
            kth = self.findKthNode(group_previous, k)

            if kth is None:
                break

            group_next = kth.next

            # Reverse the current group
            previous = group_next
            current = group_previous.next

            while current is not group_next:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node

            # Connect the reversed group to the preceding section
            old_group_start = group_previous.next
            group_previous.next = kth

            # The old first node is now the last node
            group_previous = old_group_start

        return dummy.next

    def findKthNode(
        self,
        current: Optional[ListNode],
        k: int
    ) -> Optional[ListNode]:

        while current is not None and k > 0:
            current = current.next
            k -= 1

        return current