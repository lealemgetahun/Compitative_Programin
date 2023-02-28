# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        preorder = []
        inorder = []
        self.i = 0
        def assign(node):
            if not node: return

            node.val = (node.val, self.i)
            self.i += 1
            assign(node.left)
            assign(node.right)

        assign(root)
        def pre(node):
            if not node: return

            preorder.append(node.val)
            pre(node.left)
            pre(node.right)
        def inord(node):
            if not node: return
            inord(node.left)
            inorder.append(node.val)
            inord(node.right)
        pre(root)
        inord(root)
        prestr = []
        for i in preorder:
            prestr.append((str(i[0])+","+str(i[1])))
        prestr = "*".join(prestr)
        instr = []

        for i in inorder:
            instr.append((str(i[0])+","+str(i[1])))
        instr = "*".join(instr)
     
        return prestr + " " + instr

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split()
        if not data:
            return None
        # print(data)
        preorder = data[0].split("*")
        inorder = data[1].split("*")
        # print(inorder)
        # print(preorder)
        def buildTree(preorder,inorder):
            if preorder:

                index = inorder.index(preorder[0])
                val = preorder[0].split(",")

                
                ans = TreeNode(val[0])
                ans.left = buildTree(preorder[1:index+1], inorder[:index + 1])
                ans.right = buildTree(preorder[index+1:], inorder[index+1:])
            
                return ans
        return buildTree(preorder, inorder)
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))