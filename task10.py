def count_stairs(n, prev):
    if n == 0:
        return 1
    count = 0
    for i in range(prev + 1, n + 1):
        count += count_stairs(n - i, i)
    return count

N = int(input())
print(count_stairs(N, 0))