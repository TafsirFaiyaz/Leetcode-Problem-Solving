# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        visited = set()
        n = headA
        while n:
            visited.add(n)    # Store the reference of the node
            n = n.next

        n = headB
        while n:
            if n in visited:  # if the reference is already in the set, we found the intersection
                return n
            n = n.next
        
        return None
        