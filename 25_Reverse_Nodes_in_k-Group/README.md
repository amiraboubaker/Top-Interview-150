# Intuition
We want to reverse every consecutive group of k nodes in the list. If the remaining nodes are fewer than k, leave them as is. We reverse nodes in-place using pointer manipulation.

# Approach
1. Use a dummy node pointing to head to simplify edge cases.
2. Count the total number of nodes.
3. Use two pointers: `prev` (node before current group) and `curr` (start of current group).
4. While there are at least k nodes remaining:
   - Reverse the k nodes using standard iterative reversal.
   - Connect the reversed group to the previous part of the list.
   - Move `prev` to the end of the reversed group.
5. Return `dummy.next` as the new head.

# Complexity
1. Time Complexity: O(n), each node is visited once.
2. Space Complexity: O(1), in-place reversal using only pointers.

# Code
class Solution:
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Count total nodes
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        while count >= k:
            curr = prev.next
            nex = curr.next
            # Reverse k nodes
            for _ in range(1, k):
                curr.next = nex.next
                nex.next = prev.next
                prev.next = nex
                nex = curr.next
            prev = curr
            count -= k

        return dummy.next