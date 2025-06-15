# ============================================================
# Unit 1 • Session 1
# ============================================================
#
# # Session 1 - Version 1 Problem 1: Hunny Hunt

# U — Understand
# Restate: Return the index of the first occurrence of target in the list, or -1 if not found.

# P — Plan
# Iterate through the list using index. Return index when match is found. Return -1 if loop completes.

# I — Implement
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

hunny_hunt_tests = [
    (['a', 'b', 'c'], 'b', 1),
    (['a', 'b', 'c'], 'z', -1),
    (['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn'], 'hunny', 3),
    (['bed', 'blue jacket', 'red shirt', 'hunny'], 'red balloon', -1),
    ([], 'hunny', -1),
    (['hunny'], 'hunny', 0),
    (['hunny', 'hunny'], 'hunny', 0),
    (['a', 'b', 'c', 'd'], 'd', 3),
    (['a', 'b', 'c', 'd'], 'a', 0),
    (['d', 'c', 'b', 'a'], 'b', 2),
    (['apple', 'banana', 'carrot'], 'carrot', 2),
    (['x', 'y', 'z'], 'y', 1),
    (['1', '2', '3'], '2', 1),
    (['x'], 'y', -1),
    (['hello', 'world'], 'world', 1)
]

print("\nTesting: linear_search")
for idx, (lst, target, expected) in enumerate(hunny_hunt_tests):
    result = linear_search(lst, target)
    print(f"Test {idx+1}: {result == expected}, Output: {result}, Expected: {expected}")

# ------------------------------------------------

# Session 1 - Version 1 Problem 2: Bouncy, Flouncy, Trouncy, Pouncy

# U — Understand
# Restate: Perform increment or decrement based on operation strings, starting from 1.

# P — Plan
# Track value of tigger, increment for 'bouncy'/'flouncy', decrement for 'trouncy'/'pouncy'

# I — Implement
def final_value_after_operations(operations):
    tigger = 1
    for op in operations:
        if op in ("bouncy", "flouncy"):
            tigger += 1
        else:
            tigger -= 1
    return tigger

tigger_ops_tests = [
    (["trouncy", "flouncy", "flouncy"], 2),
    (["bouncy", "bouncy", "flouncy"], 4),
    ([], 1),
    (["trouncy"], 0),
    (["flouncy"], 2),
    (["bouncy", "bouncy", "bouncy"], 4),
    (["pouncy", "pouncy", "pouncy"], -2),
    (["bouncy", "flouncy", "pouncy", "trouncy"], 1),
    (["trouncy", "trouncy", "flouncy", "flouncy"], 1),
    (["flouncy"] * 10, 11),
    (["pouncy"] * 3 + ["bouncy"] * 5, 3),
    (["bouncy", "pouncy", "bouncy", "pouncy"], 1),
    (["bouncy"] * 100, 101),
    (["pouncy"] * 100, -99),
    (["bouncy", "flouncy", "trouncy", "pouncy", "flouncy", "trouncy"], 1)
]

print("\nTesting: final_value_after_operations")
for idx, (ops, expected) in enumerate(tigger_ops_tests):
    result = final_value_after_operations(ops)
    print(f"Test {idx+1}: {result == expected}, Output: {result}, Expected: {expected}")

# ------------------------------------------------

# Session 1 - Version 1 Problem 3: T-I-Double Guh-Er II

# U — Understand
# Remove any substrings t, i, gg, and er (case insensitive) from a word.

# P — Plan
# Traverse string and skip forbidden patterns. Add remaining characters to result.

# I — Implement
def tiggerfy(word):
    i = 0
    res = ''
    while i < len(word):
        w = word[i:].lower()
        if w.startswith("gg"):
            i += 2
        elif w.startswith("er"):
            i += 2
        elif word[i].lower() in ("t", "i"):
            i += 1
        else:
            res += word[i]
            i += 1
    return res

tiggerfy_tests = [
    ("Trigger", "r"),
    ("eggplant", "eplan"),
    ("Choir", "Chor"),
    ("Tiger", "g"),
    ("giggle", "gle"),
    ("GgEr", ""),
    ("", ""),
    ("Tangier", "ang"),
    ("Integration", "negraon"),
    ("tiggertiger", "g"),
    ("ERGG", ""),
    ("pit", "p"),
    ("Ernest", "nes"),
    ("identity", "deny"),
    ("giant", "gan")  # Fixed expected value
]

print("\nTesting: tiggerfy")
for idx, (word, expected) in enumerate(tiggerfy_tests):
    result = tiggerfy(word)
    print(
        f"Test {idx+1}: {result == expected}, Output: {result}, Expected: {expected}"
    )



# ============================================================
# Unit 1 • Session 2
# ============================================================


# ------------------------------------------------
# Problem 2 — Two-Pointer Palindrome
# ------------------------------------------------
#
# U — Understand
# • Input: string s (lower-case alphabet only)
# • Output: True  → s is a palindrome
#            False → otherwise
# • Constraint: must use two-pointer technique
#
# P — Plan
# 1. l ← 0, r ← len(s) − 1
# 2. while l < r
#       · if s[l] != s[r]  → return False
#       · l ++, r --
# 3. If loop completes, return True
#
# I — Implement
def is_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


pal_tests = [
    ("madam", True),
    ("madamweb", False),
    ("", True),
    ("a", True),
    ("aa", True),
    ("ab", False),
    ("aba", True),
    ("abba", True),
    ("abcba", True),
    ("abca", False),
    ("racecar", True),
    ("leetcode", False),
    ("level", True),
    ("rotor", True),
    ("palindrome", False),
]

print("\nTesting: is_palindrome")
for idx, (s, expected) in enumerate(pal_tests, 1):
    result = is_palindrome(s)
    print(f"Test {idx}: {result == expected}, Output: {result}, Expected: {expected}")


# ------------------------------------------------
# Problem 4 — Two-Pointer Two Sum  (sorted array)
# ------------------------------------------------
#
# U — Understand
# • Input: sorted int list nums, int target
# • Output: indices [i, j] with nums[i] + nums[j] == target (exactly one solution)
# • Must not reuse same element
#
# P — Plan
# 1. l ← 0, r ← len(nums) − 1
# 2. while l < r
#       · cur = nums[l] + nums[r]
#       · if cur == target → return [l, r]
#       · if cur < target  → l ++
#         else             → r --
#
# I — Implement
def two_sum(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        cur = nums[l] + nums[r]
        if cur == target:
            return [l, r]
        if cur < target:
            l += 1
        else:
            r -= 1
    return []


two_sum_tests = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([2, 7, 11, 15], 18, [1, 2]),
    ([-3, 0, 3, 4], 0, [0, 2]),
    ([1, 2, 3, 4, 4, 9, 56, 90], 8, [3, 4]),
    ([1, 3, 5, 7], 8, [1, 2]),
    ([1, 2], 3, [0, 1]),
    ([-10, -3, 4, 11, 14], 1, [1, 2]),
    ([0, 0, 3, 4], 0, [0, 1]),
    ([1, 2, 4, 6, 10, 12], 22, [4, 5]),
    ([5, 25, 75], 100, [1, 2]),
    ([2, 3, 4], 6, [0, 2]),
    ([1, 4, 6, 8, 11], 15, [3, 4]),
    ([1, 4, 6, 8, 11], 5, [0, 1]),
    ([-5, -2, 1, 3, 6], 4, [2, 3]),
    ([1, 3, 4, 5, 6], 7, [1, 2]),
]

print("\nTesting: two_sum")
for idx, (nums, tgt, expected) in enumerate(two_sum_tests, 1):
    result = two_sum(nums, tgt)
    valid = len(result) == 2 and nums[result[0]] + nums[result[1]] == tgt
    print(f"Test {idx}: {valid}, Output: {result}, Expected: {expected}")



# ------------------------------------------------
# Problem 6 — Insert Interval
# ------------------------------------------------
#
# U — Understand
# • Input: sorted non-overlapping intervals, plus new_interval
# • Output: new list after inserting & merging overlaps
#
# P — Plan
# 1. result = []
# 2. for each [s, e] in intervals
#       · if e < new_start   → append interval (before new)
#       · elif s > new_end   → append new_interval, then
#                              reassign new_interval = [s, e]  (rest copy through)
#       · else  (overlap)    → merge: new_start = min(s, new_start)
#                                       new_end   = max(e, new_end)
# 3. append remaining new_interval
#
# I — Implement
def insert_interval(intervals, new_interval):
    ns, ne = new_interval
    output = []
    placed = False

    for s, e in intervals:
        if e < ns:                         # non-overlap, left side
            output.append([s, e])
        elif s > ne:                       # non-overlap, right side
            if not placed:
                output.append([ns, ne])
                placed = True
            output.append([s, e])
        else:                              # overlap → merge
            ns = min(ns, s)
            ne = max(ne, e)

    if not placed:
        output.append([ns, ne])
    return output


# --- 15 test-cases
interval_tests = [
    ([[1, 3], [6, 9]],           [2, 5],  [[1, 5], [6, 9]]),
    ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
                                [4, 8],   [[1, 2], [3, 10], [12, 16]]),
    ([],                        [5, 7],   [[5, 7]]),
    ([[1, 5]],                  [2, 3],   [[1, 5]]),
    ([[1, 5]],                  [2, 7],   [[1, 7]]),
    ([[1, 5]],                  [6, 8],   [[1, 5], [6, 8]]),
    ([[3, 5], [12, 15]],        [6, 6],   [[3, 5], [6, 6], [12, 15]]),
    ([[3, 5], [12, 15]],        [6, 13],  [[3, 5], [6, 15]]),
    ([[1, 2], [3, 4]],          [0, 0],   [[0, 0], [1, 2], [3, 4]]),
    ([[1, 2], [3, 4]],          [5, 6],   [[1, 2], [3, 4], [5, 6]]),
    ([[1, 2], [5, 6]],          [2, 5],   [[1, 6]]),
    ([[1, 3], [5, 7], [8, 12]], [4, 6],   [[1, 3], [4, 7], [8, 12]]),
    ([[1, 3], [5, 7], [8, 12]], [4, 13],  [[1, 3], [4, 13]]),
    ([[10, 12]],                [5, 6],   [[5, 6], [10, 12]]),
    ([[10, 12]],                [13, 15], [[10, 12], [13, 15]]),
]

print("\nTesting: insert_interval")
for idx, (intervals, new_int, expected) in enumerate(interval_tests, 1):
    result = insert_interval(intervals, new_int)
    print(f"Test {idx}: {result == expected}, Output: {result}, Expected: {expected}")
