t = int(input())
for _ in range(t):
    n, k, q = map(int, input().split())
    a = [k + 1] * n
    
    min_ranges = []
    mex_ranges = []
    
    for _ in range(q):
        c, l, r = map(int, input().split())
        l -= 1
        r -= 1
        if c == 1:
            min_ranges.append((l, r))
        else:
            mex_ranges.append((l, r))
    
    min_positions = set()
    for l, r in min_ranges:
        for i in range(l, r + 1):
            min_positions.add(i)
    
    for l, r in mex_ranges:
        vals_needed = set(range(k))
        for i in range(l, r + 1):
            if a[i] < k:
                vals_needed.discard(a[i])
        
        vals_to_place = sorted(vals_needed)
        
        for i in range(l, r + 1):
            if vals_to_place and a[i] >= k and i not in min_positions:
                a[i] = vals_to_place.pop(0)
        
        for i in range(l, r + 1):
            if vals_to_place and a[i] >= k:
                a[i] = vals_to_place.pop(0)
    
    for l, r in min_ranges:
        min_val = min(a[l:r+1])
        if min_val > k:
            a[l] = k
        elif min_val < k:
            for i in range(l, r + 1):
                if a[i] < k:
                    a[i] = k + 1
            a[l] = k
    
    print(' '.join(map(str, a)))
