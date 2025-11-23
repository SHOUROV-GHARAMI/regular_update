import sys

def solve():
    n, l, r = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    
    a.sort()
    
    left_sum = 0
    right_sum = sum(a)
    
    max_guaranteed_score = 0
    
    
    for j in range(n + 1):
        C = (right_sum - left_sum) - left_sum
        k = 2 * j - n
        
        score_at_l = C + k * l
        score_at_r = C + k * r
        
        guaranteed_score = min(score_at_l, score_at_r)
        
        if guaranteed_score > max_guaranteed_score:
            max_guaranteed_score = guaranteed_score
            
        if j < n:
            left_sum += a[j]
    
    print(max_guaranteed_score)

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()