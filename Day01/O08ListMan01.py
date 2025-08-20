l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)
l2 = [1, 2, 3, 4.5, 5.0, 6.3, 7 + 2j, 8-4j, 'nine', 'ten', 'eleven', True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 60)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 60)
# print(dir(l1))
# CRUD
#create
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

# read
print(f"l1[0] :{l1[0]}")
print(f"l1[3] :{l1[3]}")
print(f"l1[-1] :{l1[-1]}")

for i in l1:
    print(i, end=" ")
print()

print("-" * 60)
# upadate - 1. modify, 2. add values
print(f"l1 :{l1}")
l1[2]  = 300
l1[-1] = 500
print(f"l1 :{l1}")

l1[1] = 1.5
print(f"l1 :{l1}")

print("-" * 60)
# delete
print(f"l1 :{l1}")
del l1[1]
del l1[2]
print(f"l1 :{l1}")

print("-" * 60)
# add values into a list
# append, extend, insert
# check how extend and insert works

l1 = [1, 2 , 3, 4, 5]
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)
print(f"l1 :{l1}")

l1.append([9, 10, 11, 12, 13])
print(f"l1 :{l1}")

print(f"l1[8][1:4] :{l1[8][1:4]}")