
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        m=defaultdict(list)
        #self.hd=0
    
        self.verticalTraversalOperation(0,0,root,m)
        result =[]
        
        for i in sorted(m.keys()):
            temp =[]
            for j in sorted(m[i]):
                temp.append(j[1])
            result.append(temp)
            
        return result
        
    def verticalTraversalOperation(self,hd,level,root,m):
        
        if(root is None):
            return
        
        m[hd].append((level,root.val))
        
        self.verticalTraversalOperation(hd-1,level+1,root.left,m)
        self.verticalTraversalOperation(hd+1,level+1,root.right,m)
        
        