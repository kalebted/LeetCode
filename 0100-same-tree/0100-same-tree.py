# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while len(stack) != 0:
            node1, node2 = stack.pop()

            if node1 is None and node2 is None:
                continue
            
            elif node1 is None or node2 is None:
                return False

            else:
                if node1.val != node2.val:
                    return False

                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))

        return True