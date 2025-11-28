def get_value(row, col, n):
    """Get value at position (row, col) in n×n grid (0-indexed)"""
    return row * n + col + 1

def calculate_cost(row, col, n):
    """Calculate cost of cell at (row, col)"""
    cost = get_value(row, col, n)
    
    # Add neighbors: up, down, left, right
    neighbors = [
        (row - 1, col),  # up
        (row + 1, col),  # down
        (row, col - 1),  # left
        (row, col + 1)   # right
    ]
    
    for nr, nc in neighbors:
        if 0 <= nr < n and 0 <= nc < n:
            cost += get_value(nr, nc, n)
    
    return cost

def solve(n):
    """Find maximum cost by checking all cells"""
    if n == 1:
        return 1
    
    max_cost = 0
    
    # Check all cells to find maximum
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
