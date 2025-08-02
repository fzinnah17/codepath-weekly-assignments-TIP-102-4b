print("Unit 10 Session 1")

# Problem 1: is_mutual
def is_mutual(celebrities):
    n = len(celebrities)
    for i in range(n):
        for j in range(n):
            if celebrities[i][j] == 1 and celebrities[j][i] != 1:
                return False
    return True

print("\nTesting: is_mutual")
mutual_tests = [
    (
        [
            [0, 1, 1, 0],
            [1, 0, 1, 0],
            [1, 1, 0, 1],
            [0, 0, 1, 0]
        ],
        True
    ),
    (
        [
            [0, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0]
        ],
        False
    ),
    (
        [
            [0, 1],
            [1, 0]
        ],
        True
    ),
    (
        [
            [0, 1],
            [0, 0]
        ],
        False
    ),
]
for idx, (mat, expected) in enumerate(mutual_tests, 1):
    got = is_mutual(mat)
    print(f"Test {idx}: {'PASS' if got == expected else 'FAIL'} | Output: {got} | Expected: {expected}")

# --------------------------------------------------------------
# Problem 3: identify_celebrity
def identify_celebrity(trust, n):
    trust_in = [0] * (n + 1)  # 1-based index
    trust_out = [0] * (n + 1)
    for a, b in trust:
        trust_out[a] += 1
        trust_in[b] += 1
    for i in range(1, n+1):
        if trust_in[i] == n-1 and trust_out[i] == 0:
            return i
    return -1

print("\nTesting: identify_celebrity")
celebrity_tests = [
    ([[1,2]], 2, 2),
    ([[1,3],[2,3]], 3, 3),
    ([[1,3],[2,3],[3,1]], 3, -1),
    ([], 1, 1),
    ([], 2, -1),
    ([[2,3],[1,3],[3,2]], 3, -1),
    ([[2,3],[3,1],[1,2]], 3, -1),
]
for idx, (trust, n, expected) in enumerate(celebrity_tests, 1):
    got = identify_celebrity(trust, n)
    print(f"Test {idx}: {'PASS' if got == expected else 'FAIL'} | Output: {got} | Expected: {expected}")

# --------------------------------------------------------------
# Problem 4: have_connection (BFS)
def have_connection(celebs, start_celeb, target_celeb):
    from collections import deque
    n = len(celebs)
    visited = [False] * n
    q = deque([start_celeb])
    visited[start_celeb] = True
    while q:
        node = q.popleft()
        if node == target_celeb:
            return True
        for nei in range(n):
            if celebs[node][nei] == 1 and not visited[nei]:
                visited[nei] = True
                q.append(nei)
    return False

print("\nTesting: have_connection (BFS)")
cc_bfs_tests = [
    (
        [
            [0, 1, 0, 0, 0, 0, 0, 0], 
            [0, 1, 1, 0, 0, 0, 0, 0], 
            [0, 0, 0, 1, 0, 1, 0, 0], 
            [0, 0, 0, 0, 1, 0, 1, 0], 
            [0, 0, 0, 1, 0, 0, 0, 1], 
            [0, 1, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 1, 0, 0, 0, 1], 
            [0, 0, 0, 0, 1, 0, 1, 0]
        ], 
        0, 6, True
    ),
    (
        [
            [0, 1, 0, 0, 0, 0, 0, 0], 
            [0, 1, 1, 0, 0, 0, 0, 0], 
            [0, 0, 0, 1, 0, 1, 0, 0], 
            [0, 0, 0, 0, 1, 0, 1, 0], 
            [0, 0, 0, 1, 0, 0, 0, 1], 
            [0, 1, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 1, 0, 0, 0, 1], 
            [0, 0, 0, 0, 1, 0, 1, 0]
        ], 
        3, 5, False
    ),
    (
        [
            [0,1],
            [0,0]
        ],
        0, 1, True
    ),
    (
        [
            [0,1,0],
            [0,0,1],
            [0,0,0]
        ],
        0, 2, True
    ),
    (
        [
            [0,1,0],
            [0,0,1],
            [1,0,0]
        ],
        2, 1, True
    ),
    (
        [
            [0,0],
            [0,0]
        ],
        0, 1, False
    ),
]
for idx, (mat, s, t, expected) in enumerate(cc_bfs_tests, 1):
    got = have_connection(mat, s, t)
    print(f"Test {idx}: {'PASS' if got == expected else 'FAIL'} | Output: {got} | Expected: {expected}")

print("\n")
print("Unit 10 Session 2")

# Problem 1: calculate_cost

def calculate_cost(flights, start, dest):
    if start == dest:
        return 0
    
    import heapq
    pq = [(0, start)]
    visited = set()
    
    while pq:
        cost, current = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)
        if current == dest:
            return cost
        for neighbor, flight_cost in flights.get(current, []):
            if neighbor not in visited:
                heapq.heappush(pq, (cost + flight_cost, neighbor))
    return -1

print("\nTesting: calculate_cost")
flights1 = {
    'LAX': [('SFO', 50)],
    'SFO': [('LAX', 50), ('ORD', 100), ('ERW', 210)],
    'ERW': [('SFO', 210), ('ORD', 100)],
    'ORD': [('ERW', 300), ('SFO', 100), ('MIA', 400)],
    'MIA': [('ORD', 400)]
}
cost_tests = [
    (flights1, 'LAX', 'MIA', 550),  # Acceptable: 550 or 960
    (flights1, 'ERW', 'LAX', 210),
    (flights1, 'ORD', 'LAX', 100),
    (flights1, 'MIA', 'SFO', 500),
    (flights1, 'LAX', 'JFK', -1),
]
for idx, (f, start, end, expected) in enumerate(cost_tests, 1):
    got = calculate_cost(f, start, end)
    # Accept either shortest or alternate correct cost for LAX-MIA
    ok = (got in (550, 960)) if (start, end) == ('LAX', 'MIA') else (got == expected)
    print(f"Test {idx}: {'PASS' if ok else 'FAIL'} | Output: {got} | Expected: {expected}")

# Problem 3: get_itinerary
def get_itinerary(flights, source, dest):
    """
    Find shortest path using BFS - ensures minimum hops
    """
    if source == dest:
        return [source]
    
    from collections import deque
    queue = deque([(source, [source])])  # (node, path)
    visited = set([source])
    
    while queue:
        current, path = queue.popleft()
        
        # Check all neighbors
        for neighbor in flights.get(current, []):
            if neighbor == dest:
                return path + [neighbor]  # Found destination
                
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return []  # No path found


print("\nTesting: get_itinerary")
flights2 = {
    'LAX': ['SFO'],
    'SFO': ['LAX', 'ORD', 'ERW'],
    'ERW': ['SFO', 'ORD'],
    'ORD': ['ERW', 'SFO', 'MIA'],
    'MIA': ['ORD']
}
itin_tests = [
    (flights2, 'LAX', 'MIA', [['LAX','SFO','ORD','MIA'], ['LAX','SFO','ERW','ORD','MIA']]),
    (flights2, 'LAX', 'ERW', [['LAX','SFO','ERW']]),
    (flights2, 'ORD', 'SFO', [['ORD','SFO']]),
    (flights2, 'ERW', 'MIA', [['ERW','ORD','MIA']]),
]
for idx, (fl, s, d, possibles) in enumerate(itin_tests, 1):
    got = get_itinerary(fl, s, d)
    if not possibles:
        ok = got == []
    else:
        ok = any(got == ans for ans in possibles)
    print(f"Test {idx}: {'PASS' if ok else 'FAIL'} | Output: {got} | Expected: {possibles}")

# Problem 4: can_complete_flight_training
def can_complete_flight_training(num_courses, flight_prerequisites):
    prereq = {}
    for a, b in flight_prerequisites:
        prereq.setdefault(a, []).append(b)
    visiting = set()
    visited = set()

    def dfs(course):
        if course in visiting:
            return False
        if course in visited:
            return True
        visiting.add(course)
        for pre in prereq.get(course, []):
            if not dfs(pre):
                return False
        visiting.remove(course)
        visited.add(course)
        return True

    all_courses = set()
    for pair in flight_prerequisites:
        all_courses.add(pair[0])
        all_courses.add(pair[1])
    for c in all_courses:
        if not dfs(c):
            return False
    return True

print("\nTesting: can_complete_flight_training")
flight_prereqs = [
    (2, [['Advanced Maneuvers', 'Basic Navigation']], True),
    (2, [['Advanced Maneuvers', 'Basic Navigation'], ['Basic Navigation', 'Advanced Maneuvers']], False),
    (3, [['A', 'B'], ['B', 'C']], True),
    (3, [['A', 'B'], ['B', 'C'], ['C', 'A']], False),
    (1, [], True),
    (3, [], True)
]
for idx, (n, pre, expected) in enumerate(flight_prereqs, 1):
    got = can_complete_flight_training(n, pre)
    print(f"Test {idx}: {'PASS' if got == expected else 'FAIL'} | Output: {got} | Expected: {expected}")
