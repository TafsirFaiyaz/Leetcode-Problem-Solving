# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head   
        fast = head

        while fast and fast.next:  # Check if fast and fast.next are not None
            slow = slow.next        # Move slow pointer by 1
            fast = fast.next.next   # Move fast pointer by 2

            if slow == fast:     # Cycle detected
                return True

        return False
        
        
# This works by using two pointers (slow and fast) to traverse the linked list.
# If there is a cycle, the fast pointer will eventually meet the slow pointer. If there is no cycle, the fast pointer will reach the end of the list.