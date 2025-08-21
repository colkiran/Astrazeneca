l1 = []
# print(dir(l1))
print(f"l1 :{l1}")

l1.append(10)
l1.append(20)
l1.append(30)

print(f"l1 :{l1}")

print("extend".center(60 ,"-"))
l1 = list()
print(f"l1 :{l1}")
l1.extend([1, 2, 3, 4, 5])
print(f"l1 :{l1}")

l1.extend([6])
print(f"l1 :{l1}")

print("insert".center(60, "-"))
print(f"l1 :{l1}")

l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
l1.insert(7, 4.5)
l1.insert(9, 5.5)

print(f"l1 :{l1}")

print("pop".center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = l1.pop(4)
print(f"res :{res}")

res = l1.pop(8)
print(f"res :{res}")

res = l1.pop(2)
print(f"res :{res}")

res = l1.pop()   # removes the last element from the list
print(f"res :{res}")

print(f"l1 :{l1}")

print(f"remove".center(60,"-"))
l1 = [1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]

print(f"l1 :{l1}")

print("-" * 60)
l1.remove(3)
print(f"l1 :{l1}")

print("-" * 60)
l1.remove(3)
print(f"l1 :{l1}")

print("-" * 60)
l1.remove(3)
print(f"l1 :{l1}")

print("-" * 60)
while l1.count(2):
    l1.remove(2)

print(f"l1 :{l1}")
