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