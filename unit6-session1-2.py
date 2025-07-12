# ==============================================================
# Unit 6 – Session 1 (Advanced v2) · Farnaz
# ==============================================================


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# --------------------------------------------------------------
#  Problem 1 — Linked-List Game  (game_result)
# --------------------------------------------------------------
#
# U — Understand
# head: first node of even-length linked list
# Indices 0,2,… are “Even team”; 1,3,… are “Odd team”
# Each adjacent pair (even, odd) gives one point to larger value
# Return "Even", "Odd", or "Tie"
#
# P — Plan
# even_pts = odd_pts = 0
# cur = head
# while cur and cur.next:
#       even_val = cur.value
#       odd_val  = cur.next.value
#       if even_val > odd_val: even_pts += 1
#       elif odd_val > even_val: odd_pts += 1
#       cur = cur.next.next
# Compare points → return string
#
# Complexity
# n = #nodes
#   Time : O(n)    – single pass
#   Space: O(1)    – only counters
#
# I — Implement
def game_result(head):
    even_pts = odd_pts = 0
    cur = head
    while cur and cur.next:
        even_val = cur.value
        odd_val = cur.next.value
        if even_val > odd_val:
            even_pts += 1
        elif odd_val > even_val:
            odd_pts += 1
        cur = cur.next.next
    if even_pts > odd_pts:
        return "Even"
    if odd_pts > even_pts:
        return "Odd"
    return "Tie"


# --------------------------------------------------------------
#  Problem 2 — Cycle Start  (cycle_start)
# --------------------------------------------------------------
#
# U — Understand
# Given head of linked list, return .value of first node in cycle
#   or None if no cycle.
#
# P — Plan  (Floyd: tortoise-and-hare)
# 1. slow = fast = head
# 2. Move slow 1-step, fast 2-steps until:
#       fast or fast.next is None → no cycle → return None
#       slow == fast  → meeting point found
# 3. Place slow = head, keep fast at meeting point.
#    Move both 1-step until slow == fast – that node is start.
# 4. Return slow.value
#
# Complexity
# n = #nodes
#   Time : O(n)
#   Space: O(1)
#
# I — Implement
def cycle_start(path_start):
    slow = fast = path_start
    # detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    slow = path_start
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow.value


# --------------------------------------------------------------
#  Problem 4 — Calculate Prize Money  (add_two_numbers)
# --------------------------------------------------------------
#
# U — Understand
# head_a, head_b: two non-negative ints as reverse-order digits
# Return linked-list (reverse order) of their sum
#
# P — Plan
# dummy = Node(0); tail = dummy
# carry = 0
# while a or b or carry:
#       val = (a.value if a else 0) + (b.value if b else 0) + carry
#       carry, digit = divmod(val, 10)
#       tail.next = Node(digit); tail = tail.next
#       a = a.next if a else None; b = b.next if b else None
# return dummy.next
#
# Complexity
# m = len(a), n = len(b)
#   Time : O(max(m,n))
#   Space: O(max(m,n)) nodes in result (excluding input)
#
# I — Implement
def add_two_numbers(head_a, head_b):
    dummy = Node(0)
    tail = dummy
    carry = 0
    a, b = head_a, head_b
    while a or b or carry:
        val = (a.value if a else 0) + (b.value if b else 0) + carry
        carry, digit = divmod(val, 10)
        tail.next = Node(digit)
        tail = tail.next
        a = a.next if a else None
        b = b.next if b else None
    return dummy.next


# --------------------------------------------------------------
# Helper functions for tests
# --------------------------------------------------------------
def build_list(values):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return head


def build_cycle(values, pos):
    """
    Build list from values; connect last node to node at index pos.
    pos: int or None.  Returns head.
    """
    head = None
    nodes = []
    for v in reversed(values):
        head = Node(v, head)
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next
    if pos is not None and 0 <= pos < len(nodes):
        nodes[-1].next = nodes[pos]
    return head


def list_to_py(head):
    res = []
    while head:
        res.append(head.value)
        head = head.next
    return res


print("\n Testing: game_result")
gr_tests = [
    ([2, 1], "Even"),
    ([2, 5, 4, 7, 20, 5], "Odd"),
    ([4, 5, 2, 1], "Tie"),
    ([10, 3, 8, 7], "Even"),
    ([1, 11, 3, 13], "Odd"),
    ([6, 6, 6, 6], "Tie"),
    ([9, 1], "Even"),
    ([1, 9], "Odd"),
    ([5, 4, 3, 2], "Even"),
    ([2, 3, 4, 1], "Tie"),
    ([100, 99, 98, 97], "Even"),
    ([3, 4], "Odd"),
    ([7, 7, 7, 6], "Even"),
    ([5, 5, 5, 5], "Tie"),
    ([8, 0, 0, 8], "Tie"),
]
for idx, (vals, expected) in enumerate(gr_tests, 1):
    result = game_result(build_list(vals))
    print(f"Test {idx}: {result == expected}", result, expected)


print("\n Testing: cycle_start")
cs_tests = [
    (build_cycle(['A', 'B', 'C', 'D'], 1), 'B'),
    (build_cycle([1, 2, 3, 4, 5], 0), 1),
    (build_cycle([1, 2, 3], None), None),
    (build_cycle([10, 20], 0), 10),
    (build_cycle(['X'], 0), 'X'),
    (build_cycle(['p', 'q', 'r', 's'], 2), 'r'),
    (build_cycle([5, 6, 7, 8, 9], 4), 9),
    (build_cycle([5, 6, 7, 8, 9], None), None),
    (build_cycle(['start', 'mid', 'end'], 1), 'mid'),
    (build_cycle([0, 0, 0, 0], 2), 0),
    (build_cycle([1], None), None),
    (build_cycle(list(range(1, 6)), 3), 4),
    (build_cycle(['a', 'b', 'c', 'd', 'e'], None), None),
    (build_cycle([9, 8, 7], 0), 9),
    (build_cycle([2, 4, 6, 8], 2), 6),
]
for idx, (head, expected) in enumerate(cs_tests, 1):
    result = cycle_start(head)
    print(f"Test {idx}: {result == expected}", result, expected)


print("\n Testing: add_two_numbers")
at_tests = [
    ([2, 4, 3], [5, 6, 4], [7, 0, 8]),                 # 342+465=807
    ([0], [0], [0]),
    ([9, 9, 9], [1], [0, 0, 0, 1]),                     # 999+1=1000
    ([5], [5], [0, 1]),                                 # 5+5=10
    ([2, 4], [8, 5], [0, 0, 1]),                        # 42+58=100
    ([1, 8], [0], [1, 8]),
    ([9, 9], [9, 9], [8, 9, 1]),
    ([1, 0, 0, 0, 0, 0, 1], [5, 6, 4], [6, 6, 4, 0, 0, 0, 1]),
    ([7, 3], [5, 9, 2], [2, 3, 3]),                     # 37+295=332
    ([3, 2, 1], [7, 8, 9], [0, 1, 1, 1]),               # 123+987=1110
    ([6], [4, 9, 5], [0, 0, 6]),                        # 6+594=600
    ([9, 9, 9, 9], [1, 1, 1, 1], [0, 1, 1, 1, 1]),
    ([2, 4, 9], [5, 6, 4, 9], [7, 0, 4, 0, 1]),
    ([0], [7, 3, 2], [7, 3, 2]),
    ([9, 9, 1], [9, 9], [8, 9, 2]),
]
for idx, (a_vals, b_vals, expected_vals) in enumerate(at_tests, 1):
    res_head = add_two_numbers(build_list(a_vals), build_list(b_vals))
    result = list_to_py(res_head)
    print(f"Test {idx}: {result == expected_vals}", result, expected_vals)





print(f"\n")
print(f"\n")
print(f"\n")
print(f"\n")
print(f"Unit 6 Session 2 Advanced Problem Set v1")
print(f"\n")


# ==============================================================
# Session 2 Advanced Problem Set v1
# ==============================================================


# --------------------------------------------------------------
#  Problem 1 — Next in Queue  (Queue via singly-linked list)
# --------------------------------------------------------------
#
# U — Understand
# FIFO queue:  enqueue → tail,  dequeue/peek → head
#
# P — Plan
# Node class already defined.
# Queue stores:
#       self.front → head node
#       self.rear  → tail node
# is_empty():  front is None
# enqueue((song, artist)):
#       n = Node(value)
#       if empty: front = rear = n
#       else: rear.next = n ; rear = n
# dequeue():
#       if empty → None
#       else: val = front.value ; front = front.next
#             if front is None: rear = None
#             return val
# peek(): return front.value or None
#
# Complexity
#   Time:  enqueue, dequeue, peek, is_empty → O(1)
#   Space: O(1) auxiliary; queue stores k nodes (payload)
#
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # is_empty O(1)
    def is_empty(self):
        return self.front is None

    # enqueue O(1)
    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    # dequeue O(1)
    def dequeue(self):
        if self.is_empty():
            return None
        val = self.front.value
        self.front = self.front.next
        if self.front is None:          # queue became empty
            self.rear = None
        return val

    # peek O(1)
    def peek(self):
        return None if self.is_empty() else self.front.value


# helper for tests
def queue_to_list(q: Queue):
    out = []
    cur = q.front
    while cur:
        out.append(cur.value)
        cur = cur.next
    return out


print("\n Testing: Queue")
q_tests_pass = []
# 1 basic enqueue/dequeue
q = Queue()
q.enqueue(("Love Song", "Sara Bareilles"))
q.enqueue(("Ballad of Big Nothing", "Elliot Smith"))
q.enqueue(("Hug from a Dinosaur", "Torres"))
q_tests_pass.append(queue_to_list(q) == [
    ("Love Song", "Sara Bareilles"),
    ("Ballad of Big Nothing", "Elliot Smith"),
    ("Hug from a Dinosaur", "Torres"),
])
q_tests_pass.append(q.peek() == ("Love Song", "Sara Bareilles"))
q_tests_pass.append(q.dequeue() == ("Love Song", "Sara Bareilles"))
q_tests_pass.append(q.dequeue() == ("Ballad of Big Nothing", "Elliot Smith"))
q_tests_pass.append(not q.is_empty())
q_tests_pass.append(q.dequeue() == ("Hug from a Dinosaur", "Torres"))
q_tests_pass.append(q.is_empty())

# 2 enqueue after empty
q.enqueue(("Song X", "Artist X"))
q_tests_pass.append(not q.is_empty() and q.peek() == ("Song X", "Artist X"))

# 3 dequeue single element queue
q_tests_pass.append(q.dequeue() == ("Song X", "Artist X"))
q_tests_pass.append(q.is_empty())

# 4 multiple enqueue/dequeue interleaved
for i in range(3):
    q.enqueue((f"S{i}", f"A{i}"))
q_tests_pass.append(q.dequeue() == ("S0", "A0"))
q.enqueue(("S3", "A3"))
q_tests_pass.append(q.dequeue() == ("S1", "A1"))
q_tests_pass.append(q.peek() == ("S2", "A2"))
q_tests_pass.append(q.dequeue() == ("S2", "A2"))
q_tests_pass.append(q.dequeue() == ("S3", "A3"))
print(all(q_tests_pass))


# --------------------------------------------------------------
#  Problem 2 — Merge Playlists (splice list2 into list1[a…b])
# --------------------------------------------------------------
#
# U — Understand
# playlist1, playlist2 heads; indices a,b inclusive in list1 to replace
#
# P — Plan
# Walk playlist1 to node just before index a (prevA)
# Walk to node index b (afterB = node at b)
# Connect prevA.next → playlist2 head
# Find tail of playlist2, connect tail.next → afterB.next
# Edge cases: a=0 (splice at head) – treat with dummy node
#
# Complexity
# Let n = len(playlist1), m = len(playlist2)
#   Time: O(n + m)  — single traversals
#   Space: O(1)     — pointers only
#
def merge_playlists(p1, p2, a, b):
    dummy = Node(None, p1)
    prevA = dummy
    # step to node before index a
    for _ in range(a):
        prevA = prevA.next
    # node at index b
    cur = prevA.next
    for _ in range(b - a):
        cur = cur.next
    afterB = cur.next  # node after b

    # splice
    prevA.next = p2
    # find tail of p2
    tail = p2
    while tail.next:
        tail = tail.next
    tail.next = afterB
    return dummy.next


print("\n Testing: merge_playlists")
def list_from_nodes(head):
    out = []
    cur = head
    while cur:
        out.append(cur.value)
        cur = cur.next
    return out

mp_tests_pass = []
# 1 given example
p1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
p2 = Node(100, Node(101))
merged = merge_playlists(p1, p2, 2, 3)
mp_tests_pass.append(list_from_nodes(merged) == [1, 2, 100, 101, 5])

# 2 insert at head (a=0)
p1 = Node('A', Node('B', Node('C')))
p2 = Node('X', Node('Y'))
merged = merge_playlists(p1, p2, 0, 1)
mp_tests_pass.append(list_from_nodes(merged) == ['X', 'Y', 'C'])

# 3 replace tail segment
p1 = Node(10, Node(20, Node(30)))
p2 = Node(99)
merged = merge_playlists(p1, p2, 2, 2)
mp_tests_pass.append(list_from_nodes(merged) == [10, 20, 99])

# 4 whole list replaced
p1 = Node(1, Node(2))
p2 = Node(7, Node(8, Node(9)))
merged = merge_playlists(p1, p2, 0, 1)
mp_tests_pass.append(list_from_nodes(merged) == [7, 8, 9])

# 5 adjacent indices
p1 = Node('a', Node('b', Node('c', Node('d'))))
p2 = Node('x')
merged = merge_playlists(p1, p2, 1, 2)
mp_tests_pass.append(list_from_nodes(merged) == ['a', 'x', 'd'])

# 6 when playlist2 is single and replace middle
p1 = Node(1, Node(2, Node(3)))
p2 = Node(0)
merged = merge_playlists(p1, p2, 1, 1)
mp_tests_pass.append(list_from_nodes(merged) == [1, 0, 3])

# 7 playlist2 empty replacement (edge) – treat by making p2=afterB
p1 = Node(1, Node(2))
p2 = Node( ) if False else Node(None) # we don't test empty splice

# more random
import random
for _ in range(8):
    arr1 = list(range(6))
    head1 = None
    for v in reversed(arr1):
        head1 = Node(v, head1)
    arr2 = ['x', 'y']
    head2 = Node('x', Node('y'))
    merged = merge_playlists(head1, head2, 2, 4)
    mp_tests_pass.append(list_from_nodes(merged) == [0,1,'x','y',5])

print(all(mp_tests_pass))


# --------------------------------------------------------------
#  Problem 5 — Double Listening Count  (multiply by 2)
# --------------------------------------------------------------
#
# U — Understand
# monthly_listeners: linked list digits, most-significant at end
# Double the integer → return new linked list same order
#
# P — Plan
# 1. Reverse list (easy to add from head) or traverse, build stack.
#    Instead we perform in-place reverse, double with carry, then
#    reverse back.
# rev = reverse(head)
# cur = rev, carry = 0
# while cur:
#       val = cur.value*2 + carry
#       cur.value = val % 10
#       carry = val//10
#       prev = cur; cur = cur.next
# if carry: append Node(carry) to tail
# head = reverse(rev)  (restore order)
#
# Complexity
# n = #digits
#   Time : O(n)
#   Space: O(1)  (in-place)
#
def reverse_list(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


def double_listeners(monthly_listeners):
    if not monthly_listeners:
        return None
    rev = reverse_list(monthly_listeners)
    cur = rev
    carry = 0
    while cur:
        val = cur.value * 2 + carry
        cur.value = val % 10
        carry = val // 10
        prev = cur
        cur = cur.next
    if carry:
        prev.next = Node(carry)
    return reverse_list(rev)


print("\n Testing: double_listeners")
dbl_tests_pass = []
# replace only the right-hand lists
dbl_tests = [
    ([1,8,9], [3,7,8]),
    ([9,9,9], [1,9,9,8]),
    ([0], [0]),
    ([5], [1,0]),
    ([4,5,6], [9,1,2]),
    ([2,5], [5,0]),
    ([1,0,0], [2,0,0]),
    ([3,2,1], [6,4,2]),
    ([8,7], [1,7,4]),
    ([2,4,9], [4,9,8]),
    ([6,9,9,9], [1,3,9,9,8]),
    ([1,1,1,1], [2,2,2,2]),
    ([9], [1,8]),
    ([2,0,0,0], [4,0,0,0]),
    ([7,3,2], [1,4,6,4]),
]


for idx, (digits, expected) in enumerate(dbl_tests, 1):
    head = None
    for d in reversed(digits):
        head = Node(d, head)
    doubled_head = double_listeners(head)
    res = []
    cur = doubled_head
    while cur:
        res.append(cur.value)
        cur = cur.next
    dbl_tests_pass.append(res == expected)
print(all(dbl_tests_pass))

