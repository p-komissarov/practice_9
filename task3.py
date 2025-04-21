n = int(input())

max_pack = 0
best_group = 0

for k in range(2, n + 1):
    if n % k == 0:
        packs_per_person = n // k
        if packs_per_person > max_pack:
            max_pack = packs_per_person
            best_group = k

print(best_group)