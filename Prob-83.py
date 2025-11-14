# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        n = head

        while n != None and n.next != None:

            if n.val == n.next.val:
                n.next = n.next.next
                continue
                
            n = n.next

        return head