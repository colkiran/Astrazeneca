"""
result of exp = lambda var1, var2, var3.... :expression

"""
def add(x, y):
    return x + y

x = add
res = x(30, 50)
print(f"res :{res}")

print("-" * 60)

y = lambda a, b: a + b

res = y(15, 23)
print(f"res :{res}")

# lambdas are best used with - map, filter, reduce
# map - pull values from a list and pass it to lambda expression

print("map".center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

squares = list(map(lambda x : x ** 2, l1))
print(f"squares :{squares}")

print("filter".center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

evenno = list(filter(lambda x : x % 2 == 0, l1))
print(evenno)

sentence = "the quick brown fox jumps over the lazy dog"

res = list(filter(lambda x : x != 'the', sentence.split()))
print(f"res :{res}")

res = list(filter(lambda x : len(x) == 3, sentence.split()))
print(f"res :{res}")

print("reduce".center(60, "-"))
# reduce the list into a single value
from functools import reduce

l1 = [2, 7, 4, 1, 8, 3, 5, 10, 6, 9]
print(f"l1 :{l1}")

# largest number
res1 = reduce(lambda x, y: x if x > y else y, l1)
print(f"res1 :{res1}")

# smallest number
res1 = reduce(lambda x, y: x if x < y else y, l1)
print(f"res1 :{res1}")

# sum of all numbers
res2 = reduce(lambda x, y: x + y, l1)
print(f"res2 :{res2}")
