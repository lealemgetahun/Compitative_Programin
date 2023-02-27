"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        ans = new_node = Node(0)
        dic = {}
        while head:
            if head not in dic:
               dic[head] = Node(head.val)
            new_node.next = dic[head]
            if head.random not in dic:
                
                if head.random:
        
                    dic[head.random] = Node(head.random.val)
                else:
                    dic[head.random] = None
            # if head.random:
            #     print(head.random.val, head.val)
            new_node.next.random = dic[head.random]
            head = head.next
            new_node = new_node.next
        # print(dic)
        return ans.next