l1 = list(range(1, 11))
print(f"l1 :{l1}")

print("-" * 60)

for i in l1:
    if i% 2 == 0:
        print(i, end=" ")
print()

print("-" * 60)
res = [i for i in l1]
print(f"res :{res}")

print("-" * 60)
res = [i for i in l1 if i % 2 == 0]
print(f"res :{res}")

print("-" * 60)
l2 = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
print(f"l2 :{l2}")

print("-" * 60)
for i in l2:
    for j in i:
        print(j, end=" ")
print()

print("-" * 60)
res = [j for i in l2 for j in i]
print(f"res :{res}")

