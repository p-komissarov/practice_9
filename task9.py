def sum_of_dominoes(N):
    total_sum = 0
    for a in range(N + 1): 
        for b in range(a, N + 1): 
            total_sum += a + b 
    return total_sum

N = int(input())
print(sum_of_dominoes(N))