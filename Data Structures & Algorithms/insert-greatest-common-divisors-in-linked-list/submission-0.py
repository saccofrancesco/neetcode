from math import gcd

class Solution:
    def insertGreatestCommonDivisors(self, head):
        current = head

        while current.next:
            next_node = current.next

            gcd_node = ListNode(gcd(current.val, next_node.val))

            current.next = gcd_node
            gcd_node.next = next_node

            current = next_node

        return head