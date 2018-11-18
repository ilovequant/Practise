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
        queue = []
        ans = ""
        if not root:
            return ""

        queue.append(root)
        ans += str(root.val) + ','

        while queue:
            temp = ""
            n = len(queue)
            for i in range(n):
                cur = queue.pop()
                if cur.left:
                    queue.insert(0, cur.left)
                    temp += str(cur.left.val) + ','
                if not cur.left:
                    temp += '#,'
                if cur.right:
                    queue.insert(0, cur.right)
                    temp += str(cur.right.val) + ','
                if not cur.right:
                    temp += '#,'

            if len(temp) > 0:
                ans += temp

        ans = ans[:-1]
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if not data or len(data) == 0:
            return None

        readin = data.split(',')
        root = TreeNode(int(readin[0]))
        n = len(readin)
        if n == 1:
            return root
        isleft = True
        index = 0
        queue = [root]

        for i in range(1, n):
            if readin[i] is not '#':
                node = TreeNode(int(readin[i]))
                if isleft:
                    queue[index].left = node
                else:
                    queue[index].right = node
                queue.append(node)

            if not isleft:
                index += 1

            isleft = not isleft

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))