def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))

        # Find position of 1 (for increasing check) and n (for decreasing check)
        pos1 = p.index(1)
        posn = p.index(n)

        # Check increasing rotation
        inc_ok = True
        for i in range(n):
            if p[(pos1 + i) % n] != i + 1:
                inc_ok = False
                break

        # Check decreasing rotation
        dec_ok = True
        for i in range(n):
            if p[(posn + i) % n] != n - i:
                dec_ok = False
                break

        if inc_ok or dec_ok:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
