# Intuition
Two trees are the same if:
1. Both nodes are null → same.
2. Both nodes are non-null, have the same value, and their left and right subtrees are also the same.

Recursive comparison naturally fits this logic.

# Approach
1. If both nodes are null, return True.
2. If one node is null and the other is not, return False.
3. If node values differ, return False.
4. Recursively check left subtrees and right subtrees.
5. Return True only if both left and right subtrees are the same.

# Complexity
1. Time Complexity: O(n), where n is the number of nodes in the smaller tree, since each node is visited once.
2. Space Complexity: O(h), where h is the height of the tree, due to recursion stack.

# Code
class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)