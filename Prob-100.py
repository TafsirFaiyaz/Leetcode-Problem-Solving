# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self,p,q):
        if p == None and q == None:         # Both reached Trees end
            return True

        if p == None or q == None:      # One tree reached end but other not
            return False

        if p.val != q.val:      # Values not equal
            return False

        if not self.inorder(p.left, q.left):      # Left subtree comparison
            return False

        if not self.inorder(p.right, q.right):     # Right subtree comparison
            return False

        return True   # Both subtrees are same

    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        return self.inorder(p,q)
        