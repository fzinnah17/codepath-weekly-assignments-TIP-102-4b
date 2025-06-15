# ==============================================================
# Unit 3 – Session 1
# ==============================================================


# --------------------------------------------------------------
# Problem 2 — Pair Up Animals  (Min-max pair sum)
# --------------------------------------------------------------
#
# U — Understand
# • input : list discomfort_levels, even length n
# • goal  : pair animals so that the *maximum* pair sum is minimized
# • output: that minimized maximum sum
#
# P — Plan
# • Sort the list
# • Pair smallest with largest (two-pointer)
# • Record each pair sum, track the maximum
# • Return that maximum
#
# I — Implement
def pair_up_animals(discomfort_levels):
    arr = sorted(discomfort_levels)
    i, j = 0, len(arr) - 1
    best = 0
    while i < j:
        best = max(best, arr[i] + arr[j])
        i += 1
        j -= 1
    return best


# --- 15 test-cases
pair_tests = [
    ([3, 5, 2, 3], 7),
    ([3, 5, 4, 2, 4, 6], 8),
    ([1, 1], 2),
    ([1, 2, 3, 4], 5),
    ([5, 5, 5, 5], 10),
    ([1, 100, 2, 99], 101),
    ([10, 9, 8, 7, 6, 5], 15),
    ([1, 2, 4, 6, 10, 12], 13),  # 1+12=13, 2+10=12, 4+6=10 → max=13
    ([2, 2, 2, 2], 4),
    ([1, 3, 5, 9], 10),
    ([7, 1, 9, 3], 10),
    ([4, 1, 5, 9], 10),
    ([100, 200, 300, 400], 500),
    ([8, 6, 4, 2], 10),
    ([2, 8, 4, 6], 10),
]

print("\nTesting: pair_up_animals")
for idx, (levels, expected) in enumerate(pair_tests, 1):
    result = pair_up_animals(levels)
    print(f"Test {idx}: {result == expected}, Output: {result}, Expected: {expected}")


# --------------------------------------------------------------
# Problem 4 — Append Animals to Include Preference
# --------------------------------------------------------------
#
# U — Understand
# • available : current animal list string
# • preferred : target subsequence string
# • output    : min chars to append so preferred becomes subsequence
#
# P — Plan
# • Two-pointer walk:
#     j = 0  (index in preferred)
#     for ch in available:
#         if j < len(preferred) and ch == preferred[j]:
#             j += 1
# • Unmatched = len(preferred) − j  → chars we still need to append
#
# I — Implement
def append_animals(available: str, preferred: str) -> int:
    j = 0
    for ch in available:
        if j < len(preferred) and ch == preferred[j]:
            j += 1
    return len(preferred) - j


# --- 15 test-cases
append_tests = [
    ("catsdogs", "cows", 2),
    ("rabbit", "r", 0),
    ("fish", "bird", 4),
    ("abc", "abc", 0),
    ("abc", "abcd", 1),
    ("", "abc", 3),
    ("ab", "b", 0),
    ("ab", "ab", 0),
    ("ab", "ba", 1),
    ("aaaa", "aa", 0),
    ("abcd", "ce", 1),
    ("xyz", "xyzabc", 3),
    ("hello", "hello", 0),
    ("hello", "helloo", 1),
    ("abcde", "", 0),
]

print("\nTesting: append_animals")
for idx, (avail, pref, expected) in enumerate(append_tests, 1):
    result = append_animals(avail, pref)
    print(f"Test {idx}: {result == expected}, Output: {result}, Expected: {expected}")


# --------------------------------------------------------------
# Problem 6 — Validate Animal Sheltering Sequence
# --------------------------------------------------------------
#
# U — Understand
# • admitted : push order (distinct ints)
# • adopted  : desired pop order
# • Decide if adopted is a legal pop sequence from a stack
#
# P — Plan
# • Use a stack simulation:
#     i = 0 (index in admitted)
#     for each x in adopted:
#         while stack top != x:
#             if i == len(admitted): return False
#             push admitted[i]; i += 1
#         pop
# • If all popped, return True
#
# I — Implement
def validate_shelter_sequence(admitted, adopted):
    stack = []
    i = 0
    for x in adopted:
        while (not stack) or stack[-1] != x:
            if i == len(admitted):
                return False
            stack.append(admitted[i])
            i += 1
        stack.pop()
    return True


# --- 15 test-cases
shelter_tests = [
    ([1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True),
    ([1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False),
    ([1], [1], True),
    ([1, 2], [2, 1], True),
    ([1, 2, 3], [3, 2, 1], True),
    ([1, 2, 3], [1, 3, 2], True),
    ([1, 2, 3], [3, 1, 2], False),
    ([2, 1, 0], [2, 1, 0], True),
    ([2, 1, 0], [1, 2, 0], False),
    ([1, 2, 3, 4], [2, 4, 1, 3], False),
    ([1, 2, 3, 4], [1, 2, 3, 4], True),
    ([1, 2, 3, 4], [2, 3, 4, 1], True),
    ([1, 2, 3, 4], [3, 2, 4, 1], False),
    ([3, 4, 5], [5, 4, 3], True),
    ([3, 4, 5], [4, 5, 3], True),
]

print("\nTesting: validate_shelter_sequence")
for idx, (push_seq, pop_seq, expected) in enumerate(shelter_tests, 1):
    result = validate_shelter_sequence(push_seq, pop_seq)
    print(f"Test {idx}: {result == expected}, Output: {result}, Expected: {expected}")




# ==============================================================
# Unit 3 – Session 2
# ==============================================================


# --------------------------------------------------------------
# Problem 3 — Dream Corridor Design (Container With Most Water)
# --------------------------------------------------------------
#
# U — Understand
# • segments: list of widths
# • Choose i < j  → area = min(segments[i], segments[j]) * (j-i)
# • Return max area
#
# P — Plan
# • Two-pointer (left=0, right=n-1)
# • Compute area, update best
# • Move the pointer at the smaller height inward
#
# I — Implement
def max_corridor_area(segments):
    l, r = 0, len(segments) - 1
    best = 0
    while l < r:
        width = r - l
        area = min(segments[l], segments[r]) * width
        best = max(best, area)
        if segments[l] < segments[r]:
            l += 1
        else:
            r -= 1
    return best


# --- 15 test-cases
corridor_tests = [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1),
    ([4, 3, 2, 1, 4], 16),
    ([1, 2, 1], 2),
    ([2, 3, 10, 5, 7, 8, 9], 36),
    ([6, 6, 6, 6], 18),
    ([9, 8, 7, 6, 5], 20),
    ([1, 2, 3, 4, 5, 6], 9),
    ([3, 1, 2, 4, 5], 12),
    ([2, 4], 2),
    ([2, 4, 2], 4),
    ([5, 1, 2, 3, 4, 5], 25),
    ([7, 1, 2, 3, 9], 28),
    ([1, 2, 4, 3], 4),
    ([8, 6, 4, 7, 5, 3, 2], 24),
]

print("\nTesting: max_corridor_area")
for idx, (arr, expected) in enumerate(corridor_tests, 1):
    result = max_corridor_area(arr)
    print(f"Test {idx}: {result == expected}, Output: {result}, Expected: {expected}")


# --------------------------------------------------------------
# Problem 4 — Dream Building Layout (Minimum Swaps to Balance [])
# --------------------------------------------------------------
#
# U — Understand
# • s: even-length string with the same number of '[' and ']'
# • We may swap any two chars; want minimum swaps to balance
#
# P — Plan (standard algorithm)
# • Record indices of all '[' in a list pos
# • Traverse s; keep:
#     count  = balance of '[' vs ']'
#     next_i = pointer into pos
#     swaps  = total moves so far
# • When count < 0 (more ']' seen), swap current ']' with next '[':
#     swaps += pos[next_i] - cur_index
#     next_i += 1
#     count  = 1  (after virtual swap)
#
# I — Implement
def min_swaps(s):
    positions = [i for i, ch in enumerate(s) if ch == '[']
    swap_total = 0
    pos_ptr = 0
    balance = 0

    s_list = list(s)  # only needed for indexing; we do virtual swaps

    for i, ch in enumerate(s_list):
        if ch == '[':
            balance += 1
            pos_ptr += 1
        else:  # ']'
            balance -= 1

        if balance < 0:  # need swap with next '['
            swap_total += positions[pos_ptr] - i
            # virtual swap: after swap, balance becomes 1
            balance = 1
            pos_ptr += 1
    return swap_total


# --- 15 test-cases
swap_tests = [
    ("][][", 1),
    ("]]][[[", 2),
    ("[]", 0),
    ("][" , 1),
    ("[[]]", 0),
    ("[][]", 0),
    ("[[[]]]", 0),
    ("[]][[]", 1),
    ("[[[[[]]]]]", 0),
    ("][]][][", 2),
    ("[[]][][[]]", 0),
    ("][[[]]]][[", 3),
    ("][][[[]]]", 2),
    ("[[[[]]]][]", 0),
    ("[]]]]]][[[[", 3),
]

print("\nTesting: min_swaps")
for idx, (string, expected) in enumerate(swap_tests, 1):
    result = min_swaps(string)
    print(f"Test {idx}: {result == expected}, Output: {result}, Expected: {expected}")


# --------------------------------------------------------------
# Problem 6 — Time to Complete Each Dream Design (Daily Temperatures analogue)
# --------------------------------------------------------------
#
# U — Understand
# • design_times[i] = days to finish design i
# • For each i, find j > i with design_times[j] > design_times[i] (first greater)
#   answer[i] = j - i; else 0
#
# P — Plan
# • Monotonic decreasing stack of indices
# • Iterate through list:
#     while stack not empty and current value > value[stack[-1]]:
#         idx = stack.pop()
#         ans[idx] = cur_idx - idx
#     push cur_idx
#
# I — Implement
def time_to_complete_dream_designs(design_times):
    n = len(design_times)
    ans = [0] * n
    stack = []  # indices

    for i, t in enumerate(design_times):
        while stack and t > design_times[stack[-1]]:
            idx = stack.pop()
            ans[idx] = i - idx
        stack.append(i)
    return ans


# --- 15 test-cases
time_tests = [
    ([3, 4, 5, 2, 1, 6, 7, 3], [1, 1, 3, 2, 1, 1, 0, 0]),
    ([2, 3, 1, 4], [1, 2, 1, 0]),
    ([5, 5, 5, 5], [0, 0, 0, 0]),
    ([1, 2, 3, 4, 5], [1, 1, 1, 1, 0]),
    ([5, 4, 3, 2, 1], [0, 0, 0, 0, 0]),
    ([1], [0]),
    ([2, 2], [0, 0]),
    ([1, 3, 2, 4, 3], [1, 2, 1, 0, 0]),
    ([4, 3, 2, 5, 1, 6], [3, 2, 1, 2, 1, 0]),
    ([6, 5, 4, 3, 2, 1], [0, 0, 0, 0, 0, 0]),
    ([1, 1, 2, 2, 3, 3], [2, 1, 2, 1, 0, 0]),
    ([3, 6, 1, 7], [1, 2, 1, 0]),
    ([2, 1, 2, 4, 3], [2, 1, 1, 0, 0]),
    ([10, 11, 12], [1, 1, 0]),
    ([12, 11, 13, 10, 14], [2, 1, 2, 1, 0]),
]

print("\nTesting: time_to_complete_dream_designs")
for idx, (times, expected) in enumerate(time_tests, 1):
    result = time_to_complete_dream_designs(times)
    print(f"Test {idx}: {result == expected}, Output: {result}, Expected: {expected}")
