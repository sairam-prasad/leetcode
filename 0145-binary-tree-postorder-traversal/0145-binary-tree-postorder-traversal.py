# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        
        stack1, stack2= [root],[]

        while stack1:
            current = stack1.pop()
            stack2.append(current.val)

            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)
        result = stack2[::-1]
        return result