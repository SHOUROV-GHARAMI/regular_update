from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    freq = Counter(arr)
    
    deletions = 0
    for element, count in freq.items():
        if count == element:
            continue
        elif count > element:
            deletions += (count - element)
        else:
            deletions += count
    
    print(deletions)
