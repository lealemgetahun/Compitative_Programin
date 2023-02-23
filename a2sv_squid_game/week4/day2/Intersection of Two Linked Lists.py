# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA and not headB:
            return None
        len_a = self.getLength(headA)
        len_b = self.getLength(headB)
        dif = abs(len_a - len_b)
        headA, headB = (headA, headB) if len_a >= len_b else (headB, headA)
    
        for i in range(dif):
            headA = headA.next
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        # print(headA)

    def getLength(self,head):
        n = 0
        while head:
            head = head.next
            n += 1
        return n