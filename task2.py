import math

n = float(input())

while True:
    n = math.sqrt(n)
    print(f"{n:.3f}")
    if n < 2:
        break