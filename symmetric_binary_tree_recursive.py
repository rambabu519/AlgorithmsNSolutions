'''
Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

Solution : Idea is to visit each sub tree recursively from TOP to BOTTOM. Since we always need to compare two nodes, for recursive functions
we need two nodes for recursive function. Each sub tree has to satisfy following condidtions to be a symmetric:

Let us root1 and root2 are subtress passed for each recursive call.
1. Value at current nodes must be same
2. root1 left subtree and root2 right subtree must be symmetric
3. root1 right subtree and root2 left subtree must be symmetric
4. In all other cases subtrees with root nodes root1 and root2 are non-symmetric
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubTreeSymmetric(self, root1,root2):
        #If both sub trees are None then they are symmetric
        if not root1 and not root2:
            return True

        if (root1 and 
            root2 and 
            (root1.val == root2.val) and 
            self.isSubTreeSymmetric(root1.left,root2.right) and
            self.isSubTreeSymmetric(root1.right,root2.left)):
            return True
        return False

    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            #Pass initally root as two subtrees
            return self.isSubTreeSymmetric(root,root)
