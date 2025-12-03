# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n = head
        l = []
        while n!=None:
            l.append(n.val)
            n = n.next

        return l == l[::-1]
        
