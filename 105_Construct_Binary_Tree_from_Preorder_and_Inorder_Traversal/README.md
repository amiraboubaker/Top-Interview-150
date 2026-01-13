105. Construct Binary Tree from Preorder and Inorder Traversal
Solved
Medium
Topics
Companies
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Intuition

In preorder traversal, the first element is always the root of the current subtree. In inorder traversal, elements to the left of the root belong to the left subtree, and elements to the right belong to the right subtree. By locating the root position in the inorder array, the tree can be recursively reconstructed.

# Approach

1. Create a hash map to store the index of each value in the inorder array for constant-time lookups.
2. Use a pointer to track the current position in the preorder array.
3. Recursively build the tree by:
   - Selecting the current root from preorder.
   - Finding its index in inorder to determine left and right subtree boundaries.
   - Constructing the left subtree first, then the right subtree.
4. Stop recursion when the current inorder range becomes invalid.

# Complexity

- Time complexity:  
  Each node is visited once, resulting in O(n).

- Space complexity:  
  The hash map and recursion stack together require O(n) space.