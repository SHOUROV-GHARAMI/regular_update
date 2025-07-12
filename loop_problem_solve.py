if __name__ == '__main__':
    n = int(input())
    a = []
    i = 0
    while i < n:
        a.append(i)
        i += 1
        if i == n:
            break

def print_squres(numbers):
    for number in numbers:
        print(number * number)

print_squres(a)