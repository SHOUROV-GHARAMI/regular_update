def solve():
    n = int(input())
    b = list(map(int, input().split()))
    
    # Sort in descending order
    b_sorted = sorted(b, reverse=True)
    
    # Key insight: think of building the array in layers
    # At each layer transition, we need to decide the range length
    # The maximum range is constrained by:
    # 1. The formula: sum(b) - n + 1 (upper bound)
    # 2. The structure of b (we can't exceed the number of positions at each level)
    
    # For each level, count how many positions exist at that level
    # The maximum range at any level is bounded by the number of positions
    
    max_range_formula = sum(b) - n + 1
    max_range_structure = 0
    
    for i in range(n):
        current = b_sorted[i]
        next_val = b_sorted[i + 1] if i + 1 < n else 0
        
        if current > next_val:
            # At this level, we have (i+1) positions
            max_range_structure = max(max_range_structure, i + 1)
    
    # The answer is the minimum of both constraints
    print(min(max_range_formula, max_range_structure))

t = int(input())
for _ in range(t):
    solve()
