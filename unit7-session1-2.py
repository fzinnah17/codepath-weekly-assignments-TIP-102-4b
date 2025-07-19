print(f"Unit 7 Session 1")

# ==============================================================
# Farnaz Zinnah
# Unit 7 – Session 1 (Advanced PS v1)
# Problems solved:
#   1. count_layers
#   2. reverse_orders
#   6. evaluate_ternary_expression_recursive
# ==============================================================


# --------------------------------------------------------------
#  Problem 1 — Counting the Layers of a Sandwich
# --------------------------------------------------------------
#
# U — Understand
# • A sandwich is stored as nested lists:
#   ["bread", ["lettuce", ["tomato", ["bread"]]]]
# • Each inner list’s first element is a layer name (string),
#   the second (optional) item is the rest of the sandwich.
# • Return total number of layers.
#
# P — Plan
# • Base: if sandwich is **not** a list → 0  (shouldn’t happen)
# • If list length == 1 → single layer → return 1
# • Else:  1 (for current layer) + count_layers(remaining_list)
#
# Complexity
#   n = #layers
#   Time  O(n)  – one recursive visit per layer
#   Space O(n)  – call-stack depth n
#
def count_layers(sandwich):
    # not list → defensive base
    if not isinstance(sandwich, list):
        return 0
    # single element list: last layer
    if len(sandwich) == 1:
        return 1
    # first elem is current layer, second elem is rest
    return 1 + count_layers(sandwich[1])


print("\n Testing: count_layers")
cl_tests_pass = []
cl_tests = [
    (["bread", ["lettuce", ["tomato", ["bread"]]]], 4),
    (["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]], 5),
    (["bun"], 1),
    (["top", ["mid", ["low"]]], 3),
    (["a", ["b"]], 2),
    (["x", ["y", ["z", ["w", ["v"]]]]], 5),
    (["solo"], 1),
    (["one", ["two", ["three"]]], 3),
    (["first", ["second"]], 2),
    (["layer1", ["layer2", ["layer3", ["layer4"]]]], 4),
    (["bread", ["ham"]], 2),
    (["t1", ["t2", ["t3"]]], 3),
    (["end"], 1),
    (["p", ["q"]], 2),
    (["outer", ["inner1", ["inner2", ["inner3", ["inner4"]]]]], 5),
]
for idx, (sand, expected) in enumerate(cl_tests, 1):
    cl_tests_pass.append(count_layers(sand) == expected)
print(all(cl_tests_pass))


# --------------------------------------------------------------
#  Problem 2 — Reversing Deli Orders
# --------------------------------------------------------------
#
# U — Understand
# • orders: string of words separated by single spaces
# • Return string with order of words reversed (recursively).
#
# P — Plan
# • Split once into first word and “rest”.
#   If there’s no space → return orders (base).
# • Otherwise: return reverse_orders(rest) + ' ' + first_word
#
# Complexity
#   k = #words, m = length of string
#   Time  O(m) – each char processed once
#   Space O(m) – recursion depth k plus new string
#
def reverse_orders(orders: str) -> str:
    # base – no space => single word
    if ' ' not in orders:
        return orders
    first, rest = orders.split(' ', 1)
    return reverse_orders(rest) + ' ' + first



print("\n Testing: reverse_orders")
ro_tests_pass = []
ro_tests = [
    ("Bagel Sandwich Coffee", "Coffee Sandwich Bagel"),
    ("one two three", "three two one"),
    ("single", "single"),
    ("a b", "b a"),
    ("front middle back", "back middle front"),
    ("x y z w", "w z y x"),
    ("hello world again", "again world hello"),
    ("first last", "last first"),
    ("python recursion test", "test recursion python"),
    ("a b c d e", "e d c b a"),
    ("eat", "eat"),
    ("top bottom", "bottom top"),
    ("alpha beta gamma delta", "delta gamma beta alpha"),
    ("left right", "right left"),
    ("quick brown fox", "fox brown quick"),
]
for idx, (inp, exp) in enumerate(ro_tests, 1):
    ro_tests_pass.append(reverse_orders(inp) == exp)
print(all(ro_tests_pass))


# --------------------------------------------------------------
#  Problem 6 — Ternary Expression (recursive)
# --------------------------------------------------------------
#
# U — Understand
# • expression: string containing digits, T, F, '?', ':'
# • Right-to-left grouping, exactly like nested ternary.
# • Return resulting single char (digit/T/F).
#
# P — Plan
# • Use a recursive descent with an index that moves **left→right**.
#   helper() reads an operand (digit/T/F) at current index i.
#   If next char is '?' → we have ternary:               e.g.  C ? X : Y
#        condition = current char
#        skip '?' → evaluate true_branch (recursive)
#        skip ':' → evaluate false_branch (recursive)
#        return true_branch if condition == 'T' else false_branch
# • We need shared mutable index; use list [0] wrapper.
#
# Complexity
#   n = len(expression)
#   Time  O(n) – each char visited once
#   Space O(n) – recursion depth in worst right-nested case
#
def evaluate_ternary_expression_recursive(expr):
    # Base case: If expr is one char, return it.
    if len(expr) == 1:
        return expr

    # expr[0] is always the condition ('T' or 'F')
    # expr[1] is always '?'
    # Find the matching ':' for the '?' at expr[1]
    i = 2  # Start after the '?'
    depth = 0
    while i < len(expr):
        if expr[i] == '?':
            depth += 1
        elif expr[i] == ':':
            if depth == 0:
                break
            depth -= 1
        i += 1

    # Build true and false branches without slicing
    true_branch = ""
    for j in range(2, i):
        true_branch += expr[j]
    false_branch = ""
    for j in range(i + 1, len(expr)):
        false_branch += expr[j]

    if expr[0] == 'T':
        return evaluate_ternary_expression_recursive(true_branch)
    else:
        return evaluate_ternary_expression_recursive(false_branch)

te_tests = [
    ("T?2:3", "2"),
    ("F?1:T?4:5", "4"),
    ("T?T?F:5:3", "F"),
    ("F?T?1:2:3", "3"),
    ("T?9:0", "9"),
    ("F?9:0", "0"),
    ("F?F?T:1:2", "2"),
    ("T?T?T?1:2:3:4", "1"),
    ("F?T?1:2:F?3:4", "4"),
    ("T?5:F?6:7", "5"),
    ("F?5:T?6:7", "6"),
    ("T?2:3", "2"),
    ("F?1:2", "2"),
    ("T?F?T?1:0:0:9", "0"),
]

print("Testing: evaluate_ternary_expression_recursive")
all_passed = True
for idx, (expr, expected) in enumerate(te_tests, 1):
    result = evaluate_ternary_expression_recursive(expr)
    passed = result == expected
    all_passed = all_passed and passed
    print(f"Test {idx}: {'PASS' if passed else 'FAIL'} | Output: {result} | Expected: {expected}")

print("\nAll passed:", all_passed)







print(f"\n")
print(f"\n")
print(f"Unit 7 Session 2")
# ==============================================================
# Unit 7 – Session 2  ·  Advanced PS v2
# Problems solved in this file
#   1. find_affordable_ticket  – O(log n) binary search
#   3. concert_playlists       – greedy + prefix-sum + binary search
#   5. find_crescendo          – peak index in “mountain” array
# ==============================================================


# --------------------------------------------------------------
#  Problem 1 — Concert Ticket Search
# --------------------------------------------------------------
#
# U — Understand
# • prices is sorted ascending.
# • Return index of greatest price ≤ budget; if none, return -1.
#
# P — Plan  (iterative binary search O(log n))
# lo=0, hi=len(prices)-1, ans=-1
# while lo ≤ hi:
#     mid = (lo+hi)//2
#     if prices[mid] ≤ budget: ans=mid; lo=mid+1
#     else: hi = mid-1
#
# Complexity
#   Time  O(log n)
#   Space O(1)
#
def find_affordable_ticket(prices, budget):
    lo, hi = 0, len(prices) - 1
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if prices[mid] <= budget:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return ans


print("\n Testing: find_affordable_ticket")
fat_ok = []
cases1 = [
    ([50, 75, 100, 150], 90, 1),
    ([10, 20, 30], 5, -1),
    ([10, 20, 30], 10, 0),
    ([10, 20, 30], 25, 1),
    ([5, 15, 25, 35, 45], 45, 4),
    ([5, 15, 25, 35, 45], 46, 4),
    ([100], 50, -1),
    ([100], 100, 0),
    ([30, 60, 90], 60, 1),
    ([30, 60, 90], 89, 1),
    ([1,2,3,4,5], 3, 2),
    ([1,2,3,4,5], 0, -1),
    ([2,4,6,8], 7, 2),
    ([2,4,6,8], 9, 3),
    ([2,4,6,8], 1, -1),
]
for arr,bud,exp in cases1:
    fat_ok.append(find_affordable_ticket(arr,bud)==exp)
print(all(fat_ok))


# --------------------------------------------------------------
#  Problem 3 — Organizing Setlists   (concert_playlists)
# --------------------------------------------------------------
#
# U — Understand
# • song_durations: list[int]  length n
# • concert_limits: list[int]  queries m
# • For each limit, choose max #songs with total ≤ limit.
#
# P — Plan
# 1. Sort song_durations ascending  (greedy: short songs first maximise count)
# 2. Build prefix_sum array pref[i] = sum first i songs (pref[0]=0)
# 3. For each limit L: binary-search largest i where pref[i] ≤ L
#    That i is answer.
#
# Complexity
#   n = #songs, m = #queries
#   • Sorting: O(n log n)
#   • Each query: O(log n)
#   • Space: O(n) for prefix sums
#
def concert_playlists(song_durations, concert_limits):
    # Sort durations manually
    n = len(song_durations)
    for i in range(n):
        for j in range(i + 1, n):
            if song_durations[j] < song_durations[i]:
                song_durations[i], song_durations[j] = song_durations[j], song_durations[i]
    # Build prefix sums manually
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + song_durations[i]
    result = []
    # For each concert limit, use manual binary search
    for limit in concert_limits:
        lo = 0
        hi = n
        while lo < hi:
            mid = (lo + hi + 1) // 2  # search for upper bound
            if prefix[mid] <= limit:
                lo = mid
            else:
                hi = mid - 1
        result.append(lo)
    return result

cases3 = [
    ([4,3,1,2], [5,10,15], [2,4,4]),
    ([2,3,4,5], [1], [0]),
    ([1,1,1,1], [0,1,2,3,4], [0,1,2,3,4]),
    ([7,8,9], [6,7,16,24], [0,1,2,3]),
    ([3], [3], [1]),
    ([3], [2], [0]),
    ([2,2,2], [2], [1]),
    ([2,2,2], [4], [2]),
    ([2,2,2], [6], [3]),
    ([1,2,3,4,5], [5], [2]),
    ([1,2,3,4,5], [6], [3]),
    ([1,2,3,4,5], [15], [5]),
    ([100,200,300], [50,250,450,600], [0,1,2,3]),
    ([1,10,10,10], [9,10,19,20,29,30], [1,1,2,2,3,3]),
]

print("\nTesting: concert_playlists")
cp_ok = True
for idx, (sd, cl, exp) in enumerate(cases3, 1):
    res = concert_playlists(list(sd), cl)
    ok = res == exp
    cp_ok = cp_ok and ok
    print(f"Test {idx}: {'PASS' if ok else 'FAIL'} | Output: {res} | Expected: {exp}")

print("\nAll passed:", cp_ok)



# --------------------------------------------------------------
#  Problem 5 — Finding the Crescendo in a Riff   (peak index)
# --------------------------------------------------------------
#
# U — Understand
# • riff: “mountain” array – strictly increases then strictly decreases.
# • Return peak index (largest value).  O(log n).
#
# P — Plan (binary search)
# lo=0, hi=len(riff)-1
# while lo<hi:
#     mid=(lo+hi)//2
#     if riff[mid] < riff[mid+1]: lo=mid+1  (ascending)
#     else: hi=mid
# return lo
#
# Complexity  O(log n) time, O(1) space
#
def find_crescendo(riff):
    lo, hi = 0, len(riff)-1
    while lo < hi:
        mid = (lo + hi)//2
        if riff[mid] < riff[mid+1]:
            lo = mid + 1
        else:
            hi = mid
    return lo


print("\n Testing: find_crescendo")
fc_ok = []
cases5 = [
    ([1,3,7,12,10,6,2], 3),
    ([0,2,1], 1),
    ([1,5,10,9,8], 2),
    ([3,4,5,6,5,4,3], 3),
    ([1,2,3,4,5,4,3,2,1], 4),
    ([10,20,30,40,50,40,30], 4),
    ([5,6,7,8,9,10,11,12,11], 8-1),  # index 7 → value 12
    ([2,4,6,8,6,4,2], 3),
    ([1,2,3,2,1], 2),
    ([0,1,0], 1),
    ([9,8,7,6], 0),               # strictly decreasing overall but assume peak at start per mountain definition
    ([1,2], 1),                   # smallest mountain of 2 ascend?
    ([1,2,3], 2),
    ([1,3,8,12,14,13,12,9,5], 4),
    ([1,100,50], 1),
]

cases5[6]=( [5,6,7,8,9,10,11,12,11], 7 )
for arr,exp in cases5:
    fc_ok.append(find_crescendo(arr)==exp)
print(all(fc_ok))
