def get_value(row, col, n):
    return row * n + col + 1

def calculate_cost(row, col, n):
    cost = get_value(row, col, n)
    neighbors = [
        (row - 1, col),
        (row + 1, col),
        (row, col - 1),
        (row, col + 1)
    ]
    for nr, nc in neighbors:
        if 0 <= nr < n and 0 <= nc < n:
            cost += get_value(nr, nc, n)
    return cost

def solve(n):
    if n == 1:
        return 1
    max_cost = 0
    for row in range(n):
        for col in range(n):
            cost = calculate_cost(row, col, n)
            max_cost = max(max_cost, cost)
    return max_cost

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(solve(n))
