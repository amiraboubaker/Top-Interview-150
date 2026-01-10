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