from collections import Optional, TreeNode, deque, List

# 1 invert binary tree

def invertTree(root):

    if not root:
        return None
    
    tmp = root.left
    root.left = root.right
    root.right = tmp

    invertTree(root.left)
    invertTree(root.right)

    return root


# 2 max depth of a binary tree

def maxDepth(root):
    
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

# dfs
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        
        return res
    

 # 3 diameter of binary tree

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)
            nonlocal res
            res = max(res, left + right)
            return 1 + max(left, right)

        dfs(root)
        return res
# 4 balanced binary tree

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        

        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

    

   # 5 same tree

def isSameTree(p, q):

    if not p or not q:
        return False
    
    if not p or not q or p.val!= q.val:
        return False
    
    return (isSameTree(p.left, q.left) and
    isSameTree(p.right, q.right))


# 6 is subtree

def isSubTree(root, subRoot):

    if not subRoot:
        return True
    if not root:
        return False
    if sameTree(root, subRoot):
        return True
    return (sameTree(root.left, subRoot) or sameTree(root.right, subRoot))


def sameTree(s, t):
    if not s and not t:
        return True
    if not s or not t or s.val != t.val:
        return False
    return (sameTree(s.left, t.left) and sameTree(s.right, t.right))

#7 Lowest Common Ancestor in Binary Search Tree

def lowestCommonAncestor(root, p, q):
    cur = root

    while cur:

        if p.val > cur.val and q.val > cur.val:
            cur = cur.right
        elif p.val < cur.val and q.val < cur.val:
            cur = cur.left
        else:
            return cur





# 8 Binary Tree Level Order Traversal
def levelOrderTraversal(root): 
    q = deque()
    q.append(root)
    res = []


    while q:
        qLen = len(q)
        level = []
        for i in range(qLen):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        
        if level: res.appedn(level)

    return res


# 9 Binary Tree Right Side View

def rightSideView(root):
    res = []
    q = deque([root])

    while q:
        rightSide = None
        for i in range(len(q)):
            node = q.popleft()

            if node:
                rightSide = node
                q.append(node.left)
                q.append(node.right)

        if rightSide:
            res.append(rightSide.val)

    return res


# 10 Count Good Nodes in Binary Tree

def countGoodNodes(root):
    def dfs(node, maxVal):
        
        if not node:
            return 0
        
        res = 1 if node.val >= maxVal else 0
        maxVal = max(maxVal, node.val)

        res += dfs(node.left, maxVal)
        res += dfs(node.right, maxVal)
        return res
    
    return dfs(root, root.val)

# 11 Valid Binary Search Tree
def isValidBST(root):
    pass


# 12 kth smallest element
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    stack = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        k -= 1

        if k == 0:
            return curr.val
        
        curr = curr.right


#13  Construct Binary Tree from Preorder and Inorder Traversal
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root

#14 Binary Tree Maximum Path Sum

def maxPathSum(root):
    res = [root.val]

    def dfs(root):
        if not root:
            return 0
        
        leftMax = max(dfs(root.left), 0)
        rightMax = max(dfs(root.right), 0)

        res[0] = max(res[0], root.val + leftMax + rightMax)
        return root.val + max(leftMax, rightMax)
    
    dfs(root)
    return res[0]

#15 Serialize and Deserialize Binary Tree
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1

            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

