print("Unit 9 Session 1")

# ==============================================================
# Farnaz Zinnah
# Unit 9 – Session 1 (Standard PS v1)
# Problems solved:
#   1. merge_orders
#   3. max_tiers
#   5. can_fulfill_order
# ==============================================================


# Helper: Build Binary Tree from List (Level Order)
class TreeNode():
    def __init__(self, quantity, left=None, right=None):
        self.val = quantity
        self.left = left
        self.right = right

def build_tree(lst):
    if not lst or lst[0] is None:
        return None
    nodes = [TreeNode(lst[0])]
    root = nodes[0]
    idx = 1
    for node in nodes:
        if node:
            # Left child
            if idx < len(lst):
                node.left = TreeNode(lst[idx]) if lst[idx] is not None else None
                nodes.append(node.left)
                idx += 1
            # Right child
            if idx < len(lst):
                node.right = TreeNode(lst[idx]) if lst[idx] is not None else None
                nodes.append(node.right)
                idx += 1
    return root

# Helper: Print Binary Tree as List (Level Order)
def print_tree(root):
    from collections import deque
    out = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            out.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            out.append(None)
    while out and out[-1] is None:
        out.pop()
    print(out)


# --------------------------------------------------------------
#  Problem 1 — Merging Cookie Orders
# --------------------------------------------------------------
def merge_orders(o1, o2):
    if not o1 and not o2:
        return None
    if not o1:
        return o2
    if not o2:
        return o1
    merged = TreeNode(o1.val + o2.val)
    merged.left = merge_orders(o1.left, o2.left)
    merged.right = merge_orders(o1.right, o2.right)
    return merged

print("\nTesting: merge_orders")
merge_tests = [
    # (order1_list, order2_list, expected_output_list)
    ([1,3,2,5], [2,1,3,None,4,None,7], [3,4,5,5,4,None,7]),
    ([1], [2], [3]),
    ([1,None,2], [1,2], [2,2,2]),
    ([5,3,None], [2,1,3], [7,4,3])
]
def check_merge_orders(in1, in2, expected):
    t1 = build_tree(in1)
    t2 = build_tree(in2)
    merged = merge_orders(t1, t2)
    from collections import deque
    q = deque([merged])
    out = []
    while q:
        node = q.popleft()
        if node:
            out.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            out.append(None)
    # Remove trailing None
    while out and out[-1] is None:
        out.pop()
    return out

for idx, (in1, in2, expected) in enumerate(merge_tests, 1):
    result = check_merge_orders(in1, in2, expected)
    passed = result == expected
    print(f"Test {idx}: {'PASS' if passed else 'FAIL'} | Output: {result} | Expected: {expected}")



# --------------------------------------------------------------
#  Problem 3 — Maximum Tiers in Cake (DFS)
# --------------------------------------------------------------
def max_tiers(cake):
    if not cake:
        return 0
    return 1 + max(max_tiers(cake.left), max_tiers(cake.right))

print("\nTesting: max_tiers")
tiers_tests = [
    # (cake_list, expected_output)
    (["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"], 3),
    ([1], 1),
    ([1,2,3,4], 3),
    ([1,None,2,None,3], 3),
    ([1,2,None,3,None,4], 4),
    ([], 0),
    ([1,2,3,4,5,6,7], 3),
]
for idx, (lst, expected) in enumerate(tiers_tests, 1):
    root = build_tree(lst)
    result = max_tiers(root)
    passed = result == expected
    print(f"Test {idx}: {'PASS' if passed else 'FAIL'} | Output: {result} | Expected: {expected}")



# --------------------------------------------------------------
#  Problem 5 — Can Fulfill Order (Root-to-leaf path sum)
# --------------------------------------------------------------
def can_fulfill_order(inventory, order_size):
    if not inventory:
        return False
    if not inventory.left and not inventory.right:
        return inventory.val == order_size
    left = can_fulfill_order(inventory.left, order_size - inventory.val)
    right = can_fulfill_order(inventory.right, order_size - inventory.val)
    return left or right

print("\nTesting: can_fulfill_order")
fulfill_tests = [
    # (inventory_list, order_size, expected_output)
    ([5,4,8,11,None,13,4,7,2,None,None,None,1], 22, True),   # 5+4+11+2
    ([5,4,8,11,None,13,4,7,2,None,None,None,1], 2, False),
    ([1,2,3], 4, True),     # 1+2+1 or 1+3
    ([1,2], 3, True),
    ([1,2], 1, False),
    ([1,2,3], 3, True),     # 1+2
    ([1], 1, True),
    ([1], 2, False),
    ([], 0, False),
    ([2, None, 3, None, None, None, 4], 9, False),
]
for idx, (lst, order_size, expected) in enumerate(fulfill_tests, 1):
    root = build_tree(lst)
    result = can_fulfill_order(root, order_size)
    passed = result == expected
    print(f"Test {idx}: {'PASS' if passed else 'FAIL'} | Output: {result} | Expected: {expected}")



print(f"\n")
print(f"\n")
print("Unit 9 Session 2")

# ==============================================================
# Unit 9 – Session 2 (Advanced PS v1)
# Problems solved:
#   1. build_cookie_tree
#   2. count_cookie_paths
#   5. is_complete
# ==============================================================

# --------------------------------------------------------------
#  Problem 1 — Creating Cookie Orders from Descriptions
# --------------------------------------------------------------
def build_cookie_tree(descriptions):
    class TreeNode:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
    nodes = {}
    children = set()
    for parent, child, is_left in descriptions:
        if parent not in nodes:
            nodes[parent] = TreeNode(parent)
        if child not in nodes:
            nodes[child] = TreeNode(child)
        if is_left == 1:
            nodes[parent].left = nodes[child]
        else:
            nodes[parent].right = nodes[child]
        children.add(child)
    # Root is the node that was never a child
    root = None
    for parent in nodes:
        if parent not in children:
            root = nodes[parent]
            break
    return root

print("\nTesting: build_cookie_tree")
desc_tests = [
    (
        [["Chocolate Chip", "Peanut Butter", 1],
         ["Chocolate Chip", "Oatmeal Raisin", 0],
         ["Peanut Butter", "Sugar", 1]],
        ["Chocolate Chip", "Peanut Butter", "Oatmeal Raisin", "Sugar"]
    ),
    (
        [["Ginger Snap", "Snickerdoodle", 0],
         ["Ginger Snap", "Shortbread", 1]],
        ["Ginger Snap", "Shortbread", "Snickerdoodle"]
    ),
    (
        [["A", "B", 1], ["A", "C", 0]],
        ["A", "B", "C"]
    ),
]
for idx, (desc, expected) in enumerate(desc_tests, 1):
    root = build_cookie_tree(desc)
    # Level order compare
    from collections import deque
    vals = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            vals.append(node.val)
            q.append(node.left)
            q.append(node.right)
    passed = vals == expected
    print(f"Test {idx}: {'PASS' if passed else 'FAIL'} | Output: {vals} | Expected: {expected}")



# --------------------------------------------------------------
#  Problem 2 — Cookie Sum
# --------------------------------------------------------------
def count_cookie_paths(root, target_sum):
    def dfs(node, total):
        if not node:
            return 0
        total += node.val
        if not node.left and not node.right:
            return 1 if total == target_sum else 0
        return dfs(node.left, total) + dfs(node.right, total)
    return dfs(root, 0)

print("\nTesting: count_cookie_paths")
ccp_tests = [
    # ([tree_as_list], target_sum, expected)
    ([10, 5, 8, 3, 7, 12, 4], 22, 2),  # 10-5-7, 10-8-4
    ([8, 4, 12, 2, 6, None, 10], 14, 1), # 8-4-2
    ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, 1),
    ([1], 1, 1),
    ([1], 2, 0),
    ([], 0, 0),
]
for idx, (lst, target, expected) in enumerate(ccp_tests, 1):
    root = build_tree(lst)
    result = count_cookie_paths(root, target)
    passed = result == expected
    print(f"Test {idx}: {'PASS' if passed else 'FAIL'} | Output: {result} | Expected: {expected}")


# --------------------------------------------------------------
#  Problem 5 — Check Bakery Order Completeness
# --------------------------------------------------------------
def is_complete(root):
    from collections import deque
    q = deque([root])
    end = False
    while q:
        node = q.popleft()
        if not node:
            end = True
        else:
            if end:
                return False
            q.append(node.left)
            q.append(node.right)
    return True

print("\nTesting: is_complete")
complete_tests = [
    # (tree_as_list, expected)
    (["Croissant", "Cupcake", "Bagel", "Cake", "Pie", "Blondies"], True),
    (["Croissant", "Cupcake", "Bagel", "Cake", "Pie", None, "Blondies"], False),
    ([1,2,3,4,5,6,7], True),
    ([1,2,3,4,5,None,7], False),
    ([1], True),
    ([1,2], True),
    ([1,None,2], False),
]
for idx, (lst, expected) in enumerate(complete_tests, 1):
    root = build_tree(lst)
    result = is_complete(root)
    passed = result == expected
    print(f"Test {idx}: {'PASS' if passed else 'FAIL'} | Output: {result} | Expected: {expected}")

