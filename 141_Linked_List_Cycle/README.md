# Intuition
If a linked list has a cycle, moving forward node by node will eventually revisit a previously seen node. Using two pointers that move at different speeds, a fast pointer will eventually catch up to a slow pointer if a cycle exists. If there is no cycle, the fast pointer will reach the end of the list.

# Approach
1. Initialize two pointers: slow and fast, both starting at the head.
2. Move slow one step at a time and fast two steps at a time.
3. If at any point slow and fast point to the same node, a cycle exists.
4. If fast or fast.next becomes null, the list ends and there is no cycle.
5. Return true if the pointers meet, otherwise return false.

# Complexity
1. Time Complexity: O(n), because each pointer traverses the list at most a constant number of times.
2. Space Complexity: O(1), because only two pointers are used regardless of list size.

# Code
class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False