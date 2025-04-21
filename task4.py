count = 0

while True:
    N = int(input()) 
    if N == 0:
        break  
    if N % 6 == 0: 
        count += 1

print(count)