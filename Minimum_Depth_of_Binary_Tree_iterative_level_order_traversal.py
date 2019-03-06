'''
111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.  

'''
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        level = 0
		#Use list as Q
        q = [root]
		
		# while elements last in Q
        while q:
            size = len(q)
            while(size > 0):
		       #pop the first element in Q
                temp = q.pop(0)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
				# If it is a leaf node then we found min level of binary tree
                if not temp.left and not temp.right:
                    return level+1
                size -=1
            level +=  1
