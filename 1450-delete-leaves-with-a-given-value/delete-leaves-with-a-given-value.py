class Solution:
    def removeLeafNodes(self, r: Optional[TreeNode], t: int) -> Optional[TreeNode]:
        return (f:=lambda n:n and (setattr(n,'left',f(n.left)),setattr(n,'right',f(n.right))) and (n,None)[n.left==n.right==None and n.val==t])(r)