import sys

input = sys.stdin.readline


def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        a.sort(reverse=True)  # descending prices
        b.sort()  # ascending vouchers

        ans = 0
        idx = 0  # index in a

        # Step 1: pay for the k most expensive items (one per voucher)
        for i in range(k):
            ans += a[idx]
            idx += 1

        # Step 2: for each voucher, skip (x-1) cheapest products
        #         -> we add a[idx + x - 2], since the cheapest is free
        # Note: process vouchers from largest to smallest to maximize skipping
        b.reverse()
        for x in b:
            if idx + x - 1 <= n:  # group is valid
                ans += a[idx + x - 1 - 1]  # pay for last of the x-1 expensive ones
                idx += x - 1

        print(ans)


if __name__ == "__main__":
    solve()
