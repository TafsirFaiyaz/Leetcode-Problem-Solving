class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def build(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = build(l, mid-1)
            root.right = build(mid+1, r)
            return root

        return build(0, len(nums)-1)
    
    
nums = [-10,-3,0,5,9]
sol = Solution()
root = sol.sortedArrayToBST(nums)
def print_tree(node):
    if not node:
        return
    print_tree(node.left)
    print(node.val)
    print_tree(node.right)
    
print_tree(root)