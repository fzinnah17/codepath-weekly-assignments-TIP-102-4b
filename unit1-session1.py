# ✅ Session 1 - Version 1 Problem 1: Hunny Hunt

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

print("\n✅ Testing: linear_search")
for idx, (lst, target, expected) in enumerate(hunny_hunt_tests):
    result = linear_search(lst, target)
    print(f"Test {idx+1}: {result == expected}, Output: {result}, Expected: {expected}")

# ------------------------------------------------

# ✅ Session 1 - Version 1 Problem 2: Bouncy, Flouncy, Trouncy, Pouncy

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

print("\n✅ Testing: final_value_after_operations")
for idx, (ops, expected) in enumerate(tigger_ops_tests):
    result = final_value_after_operations(ops)
    print(f"Test {idx+1}: {result == expected}, Output: {result}, Expected: {expected}")

# ------------------------------------------------

# ✅ Session 1 - Version 1 Problem 3: T-I-Double Guh-Er II

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

print("\n✅ Testing: tiggerfy")
for idx, (word, expected) in enumerate(tiggerfy_tests):
    result = tiggerfy(word)
    print(f"Test {idx+1}: {result == expected}, Output: {result}, Expected: {expected}")
