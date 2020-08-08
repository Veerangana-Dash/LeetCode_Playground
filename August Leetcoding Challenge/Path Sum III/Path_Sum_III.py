# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def treeTraversal(root,target):
            
            nonlocal path
            
            if root is None:
                return 
           
            target += root.val
           
            if(target==temp):
                path +=1
            
            #frequency of target-temp upto current node
            path += h[target-temp]
            
            #addnode to hashmap for child nodes
            h[target] += 1
            
            #left sub-tree
            treeTraversal(root.left,target)
        
            #right sub-tree
            treeTraversal(root.right,target)
            
            #remove target for parallel nodes
            h[target] -=1
            
        path, temp=0, sum
        h = defaultdict(int)
        treeTraversal(root,0)
        
        return path
        