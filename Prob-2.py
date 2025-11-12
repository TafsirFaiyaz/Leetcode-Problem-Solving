#2. Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummyHead = ListNode(0)     # Creating a dummynode so that we can pass the value of result easily
        tail = dummyHead
        carry = 0                   # Initializing carry as 0


        while l1 is not None or l2 is not None or carry != 0:      # It will run as long as l1 or l2 is not None. Again, it will also run if carry is not 0 

            digit1 = l1.val if l1 is not None else 0               # checking if l1 exist. if yes then we get l1.val. else we get 0 in digit1      
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry                    # sum of l1,l2 and carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)                   # Creating a new node to connect with the tail
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None     # Checking if l1 exist. If yes we go to next node of l1. Else we get None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result
