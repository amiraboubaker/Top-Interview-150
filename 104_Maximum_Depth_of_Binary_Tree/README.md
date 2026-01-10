# Intuition
The maximum depth is the length of the longest path from the root to a leaf. For each node, the maximum depth is 1 plus the maximum depth of its left and right subtrees. This naturally leads to a recursive solution.

# Approach
1. If the current node is null, return 0 (base case).
2. Recursively find the maximum depth of the left subtree.
3. Recursively find the maximum depth of the right subtree.
4. The depth at the current node is 1 + max(left_depth, right_depth).
5. Return the depth from the root node.

# Complexity
1. Time Complexity: O(n), where n is the number of nodes, because each node is visited once.
2. Space Complexity: O(h), where h is the height of the tree, due to the recursion stack.

# Code
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)