# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        index_map = {value: i for i, value in enumerate(inorder)}
        self.pre_idx = 0

        def helper(left, right):
            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            mid = index_map[root_val]
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(inorder) - 1)

# Test
if __name__ == "__main__":
    sol = Solution()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    root = sol.buildTree(preorder, inorder)
    print("Tree constructed successfully.")  # Simple check