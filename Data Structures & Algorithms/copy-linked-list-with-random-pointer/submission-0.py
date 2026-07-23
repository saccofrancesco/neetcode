from typing import Optional

# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        next: Optional["Node"] = None,
        random: Optional["Node"] = None
    ):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None

        copies = {}

        current = head

        # Create a new node for every original node
        while current is not None:
            copies[current] = Node(current.val)
            current = current.next

        current = head

        # Connect the next and random pointers
        while current is not None:
            copied_node = copies[current]

            copied_node.next = copies.get(current.next)
            copied_node.random = copies.get(current.random)

            current = current.next

        return copies[head]