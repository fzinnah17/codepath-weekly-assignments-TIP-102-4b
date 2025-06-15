# ============================================================
# Unit 2 – Session 1 
# ============================================================

# ------------------------------------------------------------
# Problem 1 — Counting Treasure  (total_treasures)
# ------------------------------------------------------------
#
# U — Understand
# • Input: dictionary treasure_map {location: int treasures}
# • Output: total number of treasures (sum of all values)
#
# P — Plan
# 1. Return sum(treasure_map.values()).
# 2. Works for empty dict → 0.
#
# I — Implement
def total_treasures(treasure_map: dict) -> int:
    return sum(treasure_map.values())


# --- 15 test-cases
treasure_tests = [
    ({"Cove": 3, "Beach": 7, "Forest": 5}, 15),
    ({"Shipwreck": 10, "Cave": 20, "Lagoon": 15, "Peak": 5}, 50),
    ({}, 0),
    ({"X": 1}, 1),
    ({"A": 0, "B": 0}, 0),
    ({"Gold": 100, "Silver": 200}, 300),
    ({"Alpha": -5, "Beta": 5}, 0),
    ({"Spot": 9, "Hidden": 1, "Secret": 0}, 10),
    ({"One": 1, "Two": 2, "Three": 3, "Four": 4}, 10),
    ({"Pile": 999}, 999),
    ({"a": 1, "b": 1, "c": 1}, 3),
    ({"A": 2, "B": 3, "C": 4, "D": 5}, 14),
    ({"Long Beach": 7, "Deep Cave": 3}, 10),
    ({"Left": 4, "Right": 6, "Center": 8}, 18),
    ({"North": 11, "South": 12, "East": 13, "West": 14}, 50),
]

print("\nTesting: total_treasures")
for idx, (mp, expected) in enumerate(treasure_tests, 1):
    result = total_treasures(mp)
    passed = result == expected
    print(f"Test {idx}: {passed}, Output: {result}, Expected: {expected}")


# ------------------------------------------------------------
# Problem 2 — Pirate Message Check  (can_trust_message)
# ------------------------------------------------------------
#
# U — Understand
# • Input: message string (lowercase letters + whitespace)
# • Output: True  ⇢ contains every letter a-z at least once
#            False ⇢ otherwise
#
# P — Plan
# 1. Build a set of characters in message that are alphabetic.
# 2. Check len(set) == 26.
#
# I — Implement
def can_trust_message(message: str) -> bool:
    letters = {ch for ch in message if "a" <= ch <= "z"}
    return len(letters) == 26


# --- 15 test-cases
pangram_tests = [
    ("sphinx of black quartz judge my vow", True),
    ("trust me", False),
    ("the quick brown fox jumps over a lazy dog", True),
    ("abcdefghijklmnopqrstuvwxy", False),  # missing z
    ("pack my box with five dozen liquor jugs", True),
    ("", False),
    ("abcdefghijklmnopqrstuvwxyz", True),
    ("abc def ghi", False),
    ("we promptly judged antique ivory buckles for the next prize", True),
    ("five boxing wizards jump quickly", True),
    ("how vexingly quick daft zebras jump", True),
    ("a pangram? no.", False),
    ("madam im adam", False),
    ("abcdefghijklmnopqrstuvwxyz abc", True),
    ("not a full alphabet string", False),
]

print("\nTesting: can_trust_message")
for idx, (msg, expected) in enumerate(pangram_tests, 1):
    result = can_trust_message(msg)
    passed = result == expected
    print(f"Test {idx}: {passed}, Output: {result}, Expected: {expected}")


# ------------------------------------------------------------
# Problem 3 — Find All Duplicate Treasure Chests  (find_duplicate_chests)
# ------------------------------------------------------------
#
# U — Understand
# • Input: int list chests, length n, values 1..n, each appears once or twice
# • Output: list of ints that appear exactly twice (ascending order)
#
# P — Plan
# 1. seen = set(), dup = []
# 2. For each val in chests:
#       • if val in seen  → dup.append(val)
#       • else            → seen.add(val)
# 3. Return sorted(dup)  (ensures ascending)
#
# I — Implement
def find_duplicate_chests(chests):
    seen, dup = set(), []
    for val in chests:
        if val in seen:
            dup.append(val)
        else:
            seen.add(val)
    return sorted(dup)


# --- 15 test-cases
dup_tests = [
    ([4, 3, 2, 7, 8, 2, 3, 1], [2, 3]),
    ([1, 1, 2], [1]),
    ([1], []),
    ([2, 2, 2, 2], [2]),
    ([5, 4, 6, 7, 9, 3, 10, 9, 5, 6], [5, 6, 9]),
    ([1, 2, 3, 4, 5], []),
    ([1, 2, 2, 3, 3, 4, 4], [2, 3, 4]),
    ([10, 9, 8, 7, 10, 8, 9], [8, 9, 10]),
    ([6, 5, 4, 3, 2, 1], []),
    ([1, 1, 1, 2, 2, 3, 3], [1, 2, 3]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], []),
    ([2, 1, 4, 3, 4, 5], [4]),
    ([3, 3, 3, 3, 3], [3]),
    ([7, 8, 9, 7, 9, 8], [7, 8, 9]),
    ([11, 12, 13, 11, 12, 14, 15, 15], [11, 12, 15]),
]

print("\nTesting: find_duplicate_chests")
for idx, (arr, expected) in enumerate(dup_tests, 1):
    result = find_duplicate_chests(arr)
    passed = result == expected
    print(f"Test {idx}: {passed}, Output: {result}, Expected: {expected}")



# ==============================================================
# Unit 2 – Session 2
# ==============================================================

# --------------------------------------------------------------
# Problem 1 — Cook Off  (max_attempts)
# --------------------------------------------------------------
#
# U — Understand
# • inputs:  ingredients  → string of letters on hand
#            target_meal  → recipe string we must form
# • output:  maximum number of full copies of target_meal
#
# P — Plan
# 1. Count each letter in ingredients  (Counter)
# 2. Count each letter in target_meal  (Counter)
# 3. For every required letter c:
#       copies_c = floor(ingredients[c] / need[c])
# 4. The answer is min(copies_c) over all required letters
#    (If any letter missing ⇒ 0)
#
# I — Implement
from collections import Counter
import math

def max_attempts(ingredients: str, target_meal: str) -> int:
    need = Counter(target_meal)
    have = Counter(ingredients)
    # infinity placeholder large number
    best = math.inf
    for ch, cnt in need.items():
        if have[ch] == 0:
            return 0
        best = min(best, have[ch] // cnt)
    return 0 if best is math.inf else best


# --- 15 test-cases
cook_tests = [
    ("aabbbcccc", "abc", 2),
    ("ppppqqqrrr", "pqr", 3),
    ("ingredientsforcooking", "cooking", 1),
    ("aaa", "aaaa", 0),
    ("abc", "abcd", 0),
    ("aaaaaa", "aa", 3),
    ("abcabcabc", "abc", 3),
    ("xyzxyz", "zz", 1),
    ("zzz", "zz", 1),
    ("aaaaabbbbb", "ab", 5),
    ("aaaaaaaaa", "a", 9),
    ("bbbbbb", "bb", 3),
    ("", "a", 0),
    ("abcabc", "aabbcc", 1),
    ("aaaaabbbbbbccccc", "abc", 5),
]

print("\nTesting: max_attempts")
for idx, (ing, meal, expected) in enumerate(cook_tests, 1):
    result = max_attempts(ing, meal)
    print(f"Test {idx}: {result == expected}, Output: {result}, Expected: {expected}")


# --------------------------------------------------------------
# Problem 3 — Cows and Bulls  (get_hint)
# --------------------------------------------------------------
#
# U — Understand
# • inputs: secret, guess  (equal-length numeric strings)
# • output: hint "xAyB" where
#       x = bulls (digit correct & position correct)
#       y = cows  (digit present but position wrong)
#
# P — Plan
# 1. Iterate positions i:
#       if secret[i] == guess[i] → bulls++
#       else:
#           count unmatched secret digits in s_cnt
#           count unmatched guess digits  in g_cnt
# 2. cows = Σ  min(s_cnt[d], g_cnt[d]) for each digit d
# 3. return f"{bulls}A{cows}B"
#
# I — Implement
from collections import defaultdict

def get_hint(secret: str, guess: str) -> str:
    bulls = 0
    s_cnt = defaultdict(int)
    g_cnt = defaultdict(int)

    for s, g in zip(secret, guess):
        if s == g:
            bulls += 1
        else:
            s_cnt[s] += 1
            g_cnt[g] += 1

    cows = sum(min(s_cnt[d], g_cnt[d]) for d in s_cnt)
    return f"{bulls}A{cows}B"


# --- 15 test-cases
hint_tests = [
    ("1807", "7810", "1A3B"),
    ("1123", "0111", "1A1B"),
    ("1234", "1234", "4A0B"),
    ("1234", "4321", "0A4B"),
    ("1234", "5678", "0A0B"),
    ("11", "11", "2A0B"),
    ("11", "10", "1A0B"),
    ("1122", "2211", "0A4B"),
    ("1122", "1222", "3A0B"),
    ("5678", "5768", "2A2B"),
    ("0000", "0000", "4A0B"),
    ("0000", "1111", "0A0B"),
    ("123456", "654321", "0A6B"),
    ("1123", "1111", "2A0B"),
    ("9305", "3095", "1A3B"),
]

print("\nTesting: get_hint")
for idx, (sec, gue, expected) in enumerate(hint_tests, 1):
    result = get_hint(sec, gue)
    print(f"Test {idx}: {result == expected}, Output: {result}, Expected: {expected}")


# --------------------------------------------------------------
# Problem 5 — Assign Unique Nicknames  (assign_unique_nicknames)
# --------------------------------------------------------------
#
# U — Understand
# • input:  list of requested nicknames
# • output: list with unique nicknames (suffix "(k)" added as needed)
#
# P — Plan
# 1. used = set()           · all assigned names
#    next_k = dict()        · base → next suffix integer to try
# 2. For each name in nicknames:
#       if name not in used:
#           assign = name
#           used.add(assign)
#           next_k.setdefault(name, 1)
#       else:
#           k = next_k[name]
#           while f"{name}({k})" in used:
#               k += 1
#           assign = f"{name}({k})"
#           used.add(assign)
#           next_k[name] = k + 1
#           next_k.setdefault(assign, 1)   # handle future dups of new name
# 3. Append assign to result list
#
# I — Implement
def assign_unique_nicknames(nicknames):
    used = set()
    next_k = {}
    res = []

    for name in nicknames:
        if name not in used:
            assigned = name
            used.add(assigned)
            next_k.setdefault(name, 1)
        else:
            k = next_k[name]
            while True:
                candidate = f"{name}({k})"
                if candidate not in used:
                    assigned = candidate
                    used.add(assigned)
                    next_k[name] = k + 1
                    next_k.setdefault(candidate, 1)
                    break
                k += 1
        res.append(assigned)
    return res


# --- 15 test-cases
nick_tests = [
    (["Champ","Diva","Champ","Ace"],
     ["Champ","Diva","Champ(1)","Ace"]),

    (["Ace","Ace","Ace","Maverick"],
     ["Ace","Ace(1)","Ace(2)","Maverick"]),

    (["Star","Star","Star","Star","Star"],
     ["Star","Star(1)","Star(2)","Star(3)","Star(4)"]),

    (["Hero"],
     ["Hero"]),

    (["Hero","Hero"],
     ["Hero","Hero(1)"]),

    (["Hero","Hero","Hero"],
     ["Hero","Hero(1)","Hero(2)"]),

    (["X","Y","X","Y"],
     ["X","Y","X(1)","Y(1)"]),

    (["Dog","Dog(1)","Dog"],
     ["Dog","Dog(1)","Dog(2)"]),

    (["Cat","Cat","Cat(1)"],
     ["Cat","Cat(1)","Cat(2)"]),

    (["A","A(1)","A(1)"],
     ["A","A(1)","A(1)(1)"]),

    (["D","D","D","D","D"],
     ["D","D(1)","D(2)","D(3)","D(4)"]),

    (["Z(1)","Z(1)"],
     ["Z(1)","Z(1)(1)"]),

    (["M","N","O"],
     ["M","N","O"]),

    (["AA","AA","BB","AA","BB"],
     ["AA","AA(1)","BB","AA(2)","BB(1)"]),

    (["foo","foo","foo(1)","foo(1)","foo(2)"],
     ["foo","foo(1)","foo(1)(1)","foo(1)(2)","foo(2)"]),
]

print("\nTesting: assign_unique_nicknames")
for idx, (input_names, expected) in enumerate(nick_tests, 1):
    result = assign_unique_nicknames(input_names)
    passed = result == expected
    print(f"Test {idx}: {passed}, Output: {result}, Expected: {expected}")
