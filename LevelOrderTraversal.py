# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class LevelOrderTraversal(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = []
        ans = []
        if root is None:
            return queue

        queue.insert(0, root)
        ans.append([root.val])

        while (queue):
            n = len(queue)
            temp = []
            for i in range(0, n):
                node = queue.pop()
                if node.left:
                    queue.insert(0, node.left)
                    temp.append(node.left.val)
                if node.right:
                    queue.insert(0, node.right)
                    temp.append(node.right.val)
            if temp:
                ans.append(temp)

        return ans


#test case?