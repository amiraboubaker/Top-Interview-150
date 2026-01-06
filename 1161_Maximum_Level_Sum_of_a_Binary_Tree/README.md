# 1161. Maximum Level Sum of a Binary Tree

Mira  
0  
a few seconds ago  
Python  

## Intuition
The goal is to find the level in a binary tree that has the maximum sum of node values. Since trees are naturally explored level by level, using a breadth-first search (BFS) makes the most sense. This allows us to calculate the sum of each level as we traverse the tree from top to bottom.

## Approach
We use a queue to perform a level-order traversal starting from the root. For each level, we calculate the sum of all node values by iterating over the number of nodes currently in the queue. While processing a level, we add each node's children to the queue for the next level. We keep track of the maximum level sum encountered and store the corresponding level number. After traversing the entire tree, we return the level with the highest sum.

## Complexity
**Time complexity:**  
O(n), where n is the number of nodes in the tree, since each node is visited once.

**Space complexity:**  
O(n), due to the queue storing nodes during the breadth-first traversal.

## Code
```python
from collections import deque

class Solution:
    def maxLevelSum(self, root):
        queue = deque([root])
        max_sum = float('-inf')
        max_level = 1
        level = 1
        
        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
            level += 1
        
        return max_level
```