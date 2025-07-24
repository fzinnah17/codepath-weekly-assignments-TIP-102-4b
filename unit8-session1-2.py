print(f"Unit 8 Session 1")

# ==============================================================
# Farnaz Zinnah
# Unit 8 – Session 1 (Advanced PS v1)
# Problems solved:
#   1. max_depth
#   2. sum_of_left_leaves
#   6. lowest_common_ancestor
# ==============================================================

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# --------------------------------------------------------------
#  Problem 1 — Maximum Depth of Binary Tree
# --------------------------------------------------------------
#
# U — Understand
# • Input: Root node of a binary tree.
# • Output: Integer, max depth from root to any leaf.
# • Edge: Empty tree returns 0.
#
# P — Plan
# • If root is None, return 0.
# • Recursively get max depth of left and right subtrees.
# • Return 1 + max(left, right).
#
# Complexity
#   n = number of nodes
#   Time  O(n)  – visit every node once
#   Space O(h)  – call-stack, h = height
#
def max_depth(root):
    if root is None:
        return 0
    left = max_depth(root.left)
    right = max_depth(root.right)
    return 1 + (left if left > right else right)

print("\nTesting: max_depth")
t1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
t2 = TreeNode(1, None, TreeNode(2))
print(max_depth(t1), "Expected: 3")
print(max_depth(t2), "Expected: 2")
print(max_depth(None), "Expected: 0")

# --------------------------------------------------------------
#  Problem 2 — Sum of Left Leaves
# --------------------------------------------------------------
#
# U — Understand
# • Input: Root node of binary tree.
# • Output: Sum of values of all left leaves.
# • Leaf: node with no left/right child.
#
# P — Plan
# • Traverse recursively.
# • If left child exists and is a leaf, add its value.
# • Recursively sum for left and right subtrees.
#
# Complexity
#   n = number of nodes
#   Time  O(n)
#   Space O(h)
#
def sum_of_left_leaves(root):
    if root is None:
        return 0
    total = 0
    if root.left and (root.left.left is None and root.left.right is None):
        total += root.left.val
    total += sum_of_left_leaves(root.left)
    total += sum_of_left_leaves(root.right)
    return total

print("\nTesting: sum_of_left_leaves")
# Tree:      3
#         /     \
#        9      20
#             /    \
#           15      7
t3 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(sum_of_left_leaves(t3), "Expected: 24")   # 9 + 15

t4 = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
print(sum_of_left_leaves(t4), "Expected: 6")    # 2 + 4

t5 = TreeNode(1)
print(sum_of_left_leaves(t5), "Expected: 0")

# --------------------------------------------------------------
#  Problem 6 — Lowest Common Ancestor (LCA) of Binary Tree
# --------------------------------------------------------------
#
# U — Understand
# • Input: Root, two nodes p, q.
# • Output: Node where both p and q split (lowest ancestor).
# • Edge: One node can be ancestor of itself.
#
# P — Plan
# • If root is None or matches p or q, return root.
# • Search left and right subtrees.
# • If both sides are non-null, root is LCA.
# • Else return non-null child.
#
# Complexity
#   n = number of nodes
#   Time  O(n)
#   Space O(h)
#
def lowest_common_ancestor(root, p, q):
    if root is None or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right

print("\nTesting: lowest_common_ancestor")
# Tree:       3
#           /   \
#          5     1
#         / \   / \
#        6   2 0   8
#           / \
#          7   4
n7 = TreeNode(7)
n4 = TreeNode(4)
n2 = TreeNode(2, n7, n4)
n6 = TreeNode(6)
n5 = TreeNode(5, n6, n2)
n0 = TreeNode(0)
n8 = TreeNode(8)
n1 = TreeNode(1, n0, n8)
t6 = TreeNode(3, n5, n1)

lca = lowest_common_ancestor(t6, n5, n1)
print(lca.val if lca else None, "Expected: 3")
lca = lowest_common_ancestor(t6, n5, n4)
print(lca.val if lca else None, "Expected: 5")
lca = lowest_common_ancestor(t6, n7, n4)
print(lca.val if lca else None, "Expected: 2")
lca = lowest_common_ancestor(t6, n6, n7)
print(lca.val if lca else None, "Expected: 5")



print(f"\n")
print(f"\n")
print(f"Unit 8 Session 2")

# ==============================================================
# Farnaz Zinnah
# Unit 8 – Session 2 (Advanced PS v1)
# Problems solved:
#   1. sort_plants
#   2. find_flower
#   4. remove_plant
# ==============================================================


# --------------------------------------------------------------
#  Problem 1 — Sorting Plants by Rarity (BST Inorder Traversal)
# --------------------------------------------------------------
#
# U — Understand
# • Input: root of BST (TreeNode with key=rarity, val=name)
# • Output: List of (key, val) tuples, sorted by key ascending (least to most rare)
# • BST property: left < root < right by key
#
# P — Plan
# • Do inorder traversal (left, root, right)
# • Build result list as you go
#
# Complexity
#   n = # nodes
#   Time  O(n)  – visit every node
#   Space O(h)  – call stack, h=height
#
class TreeNode:
    def __init__(self, val, key, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

def sort_plants(collection):
    res = []
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        res.append((node.key, node.val))
        inorder(node.right)
    inorder(collection)
    return res

# Helper to build a tree for demo/testing (simple)
def build_tree(values):
    nodes = [TreeNode(v[1], v[0]) if v else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

print("\nTesting: sort_plants")
values = [
    (3, "Monstera"), 
    (1, "Pothos"), 
    (5, "Witchcraft Orchid"), 
    None, 
    (2, "Spider Plant"), 
    (4, "Hoya Motoskei")
]
collection = build_tree(values)
print(sort_plants(collection))
# Expected: [(1, 'Pothos'), (2, 'Spider Plant'), (3, 'Monstera'), (4, 'Hoya Motoskei'), (5, 'Witchcraft Orchid')]


# --------------------------------------------------------------
#  Problem 2 — Flower Finding (BST search by value)
# --------------------------------------------------------------
#
# U — Understand
# • Input: root of BST (TreeNode, val is name), string name
# • Output: True if name in BST, else False
# • BST property: left < root < right by val (alphabetical)
#
# P — Plan
# • Compare name to node.val:
#    - If same, return True
#    - If name < node.val, search left
#    - If name > node.val, search right
#
# Complexity
#   n = # nodes
#   h = height (log n if balanced)
#   Time  O(h)
#   Space O(h) (recursion stack)
#
class NameTreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def find_flower(inventory, name):
    cur = inventory
    while cur:
        if cur.val == name:
            return True
        elif name < cur.val:
            cur = cur.left
        else:
            cur = cur.right
    return False

def build_tree_names(values):
    nodes = [NameTreeNode(v) if v else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

print("\nTesting: find_flower")
values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree_names(values)
print(find_flower(garden, "Lilac"))     # True
print(find_flower(garden, "Sunflower")) # False


# --------------------------------------------------------------
#  Problem 4 — Remove Plant (BST delete node by value)
# --------------------------------------------------------------
#
# U — Understand
# • Input: root of BST (by val), string name to remove
# • Output: root of BST after removing node with value name
# • If node has two children: replace with inorder predecessor (max left subtree)
#
# P — Plan
# • If name < node.val: go left
# • If name > node.val: go right
# • If node found:
#     - If no left: return right
#     - If no right: return left
#     - If both: find rightmost in left, swap values, delete rightmost in left
#
# Complexity
#   n = # nodes
#   h = height
#   Time  O(h)
#   Space O(h)
#
class RemoveTreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def remove_plant(collection, name):
    def remove(node, name):
        if not node:
            return None
        if name < node.val:
            node.left = remove(node.left, name)
        elif name > node.val:
            node.right = remove(node.right, name)
        else:
            # Node found
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # Both children: find predecessor (max in left subtree)
            pred = node.left
            while pred.right:
                pred = pred.right
            node.val = pred.val
            node.left = remove(node.left, pred.val)
        return node
    return remove(collection, name)

def build_tree_remove(values):
    nodes = [RemoveTreeNode(v) if v else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

def print_tree(root):
    # Level order print (None for missing children)
    from collections import deque
    result = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            result.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            result.append(None)
    # Remove trailing None's
    while result and result[-1] is None:
        result.pop()
    print(result)

print("\nTesting: remove_plant")
values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
collection = build_tree_remove(values)
print_tree(remove_plant(collection, "Pilea"))
# Expected: ['Money Tree', 'Hoya', 'Orchid', None, 'Ivy', None, 'ZZ Plant']

