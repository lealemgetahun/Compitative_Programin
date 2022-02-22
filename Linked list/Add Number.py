# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = start = ListNode()
        carry = 0
        while l1 != None or l2 != None or carry > 0:
            num1  =0
            num2 = 0
          
            if l1 != None:
                num1 = l1.val
                l1 = l1.next
            if l2 != None:
                num2 = l2.val
                l2 = l2.next
            temp = num1 + num2 + carry
            
            carry = temp // 10
            new = ListNode(temp%10)
            res.next = new
            res = res.next
                
       
    
    
        return start.next