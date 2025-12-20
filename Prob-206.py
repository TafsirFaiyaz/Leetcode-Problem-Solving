# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next     # store next node
            curr.next = prev          # reverse the link
            prev = curr               # move prev to current node
            curr = next_node          # move to next node

        return prev