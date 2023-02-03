# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)

        queue = deque()
        queue.append((root, 0, 0))

        while queue:
            size = len(queue)
            cols = defaultdict(list)
            for _ in range(size):
                node, row, col = queue.popleft()
                cols[col].append(node.val)
                if node.left:
                    queue.append((node.left, row + 1, col - 1))
                if node.right:
                    queue.append((node.right, row + 1, col + 1))
            for col in cols:
                dic[col].extend(sorted(cols[col]))
        ans = []
        for key in sorted(dic):
            ans.append(dic[key])
        return ans
                

