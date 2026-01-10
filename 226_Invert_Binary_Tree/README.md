# Intuition
Inverting a binary tree means swapping the left and right children of every node. This can be done recursively: invert the left and right subtrees, then swap them at the current node.

# Approach
1. If the node is null, return null.
2. Recursively invert the left subtree.
3. Recursively invert the right subtree.
4. Swap the left and right children of the current node.
5. Return the current node.

# Complexity
1. Time Complexity: O(n), each node is visited once.
2. Space Complexity: O(h), where h is the height of the tree due to recursion stack.

# Code
class Solution:
    def invertTree(self, root):
        if not root:
            return None
        # Invert left and right subtrees
        left_inverted = self.invertTree(root.left)
        right_inverted = self.invertTree(root.right)
        # Swap them
        root.left, root.right = right_inverted, left_inverted
        return root