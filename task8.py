import math

def count_ways(x):
    count = 0
    for a in range(1, int(math.sqrt(x)) + 1):
        b_squared = x - a**2
        b = int(math.sqrt(b_squared))
        if b * b == b_squared and b >= a:
            count += 1
    return count

x = int(input())
print(count_ways(x))