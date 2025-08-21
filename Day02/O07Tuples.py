
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))

print("-" * 60)
t2 = (1, 2, 3.4, 4.0, 5+2j, 6-3j, True, False, 'eight', 'nine', 'ten')
print(f"t2 :{t2}")
print(type(t2))

print("-" * 60)
t3 = tuple(range(10, 101, 10))
print(f"t3 :{t3}")
print(type(t3))

print("-" * 60)
t4 = 10,
print(f"t4 :{t4}")
print(type(t4))

print("-" * 60)
t5 = 1, 2, 3, 4, 5
print(f"t5 :{t5}")
print(type(t5))

print("-" * 60)
# print(dir(t1))

# count - count of a value that gets repeated
# index - returns the index of a value

print(f"t5 :{t5}")
print(f"t5[0] :{t5[0]}")
# t1[0] = 100 - tuples are immutable