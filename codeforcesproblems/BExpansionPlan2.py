t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    s = input().strip()
    x, y = abs(x), abs(y)
    for i in range(n - 1, -1, -1):
        if x == 0 and y == 0:
            print("YES")
            break
        if s[i] == '8':
            if x > y:
                x -= 1
            elif y > x:
                y -= 1
            else:
                x -= 1
                y -= 1
        else:
            if x > 0 and y > 0:
                if max(x, y) <= i:
                    print("YES")
                else:
                    print("NO")
                break
            if x > 0:
                x -= 1
            if y > 0:
                y -= 1
    else:
        print("YES" if x == 0 and y == 0 else "NO")


