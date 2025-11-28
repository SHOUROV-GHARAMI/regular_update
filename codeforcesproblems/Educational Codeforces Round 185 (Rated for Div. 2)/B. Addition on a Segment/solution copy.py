def solve():
    n = int(input())
    b = list(map(int, input().split()))
    
    b_sorted = sorted(b, reverse=True)
    
    max_range_formula = sum(b) - n + 1
    max_range_structure = 0
    
    for i in range(n):
        current = b_sorted[i]
        next_val = b_sorted[i + 1] if i + 1 < n else 0
        
        if current > next_val:
            max_range_structure = max(max_range_structure, i + 1)
    
    print(min(max_range_formula, max_range_structure))

t = int(input())
for _ in range(t):
    solve()
