# Intuition
A tree is symmetric if the left subtree is a mirror of the right subtree. For two trees to be mirror images:
1. Their root values must be equal.
2. The left child of one tree is the mirror of the right child of the other, and vice versa.

# Approach (Recursive)
1. Define a helper function `isMirror(t1, t2)`:
   - If both nodes are null, return True.
   - If only one is null or values differ, return False.
   - Recursively check: `isMirror(t1.left, t2.right)` and `isMirror(t1.right, t2.left)`.
2. Call `isMirror(root.left, root.right)` on the root.

# Complexity
1. Time Complexity: O(n), each node is visited once.
2. Space Complexity: O(h), recursion stack, where h is the height of the tree.

# Code (Recursive)
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        
        return isMirror(root.left, root.right)