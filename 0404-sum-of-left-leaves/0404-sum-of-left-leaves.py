# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        stack = [(root, False, False)]
        summation = 0

        while len(stack) != 0:
            node, visited, left = stack.pop()

            if node is not None:
                if visited == True:
                    if left == True:
                        if node.right is None and node.left is None:
                            summation += node.val
                else:
                    stack.append((node, True, left))

                    if node.right is not None:
                        stack.append((node.right, False, False))
                    if node.left is not None:
                        stack.append((node.left, False, True))
        return summation