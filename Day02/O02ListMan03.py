
print("count".center(60, "-"))
l1 = [1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]

print(f"l1 :{l1}")

print('-' * 60)
print(f"1 :{l1.count(1)}")
print(f"2 :{l1.count(2)}")
print(f"3 :{l1.count(3)}")
print(f"5 :{l1.count(5)}")

print("index".center(60,"-"))
l1 = [1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]

print(f"l1 :{l1}")

print('-' * 60)
print(l1.index(3))
print(l1.index(3, l1.index(3) + 1))
print(l1.index(3, l1.index(3, l1.index(3) + 1 )+ 1))

print("sort".center(60, "-"))
"""
sort   - will sort the original list
sorted - will take a copy of the list and sort
"""
l1 = [8, 4, 6, 10, 1, 5, 9, 2, 7, 3]
print(f"l1 :{l1}")
res_asc = sorted(l1)
print(f"Ascending Order :{res_asc}")
res_desc = sorted(l1, reverse=True)
print(f"Descending Order :{res_desc}")

print("-" * 60)
l1 = [8, 'zebra', 'apple', 4, 'yellow', 'blue', 6, 'white', 'orange', 10, 'violet', 'pink',  1, 'dog', 'xray', 5, 'green', 'maroon', 9, 'egg', 'frog', 2,'lion', 7, 3, 130, 1034, 29, 265, 2134]

print(f"l1 :{l1}")
print('-' * 60)

asc = sorted(l1, key=ascii)
for i in range(0, len(l1)):
    if type(asc[i]) == int:
        # print(i)
        break

print(f"Ascending :{asc[:15] + sorted(asc[15:])}")

"""
cities = ['thiruvananthapuram', 'chennai', 'pune', 'mumbai', 'bangalore', 'hyderabad', 'vishakapatnam', 'ooty', 'mysore', 'kolkata', 'delhi'] 
sort it based on the length of each city
"""

print("copy".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

# copy the list l1 to l2
l2 = l1         # shallow copy - share the data and the address

print(f"l2 before:{l2}")
l2.append(6)
l2.append(7)
l2.append(8)

print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("-" * 60)
print("-" * 60)

l3 = [10, 20, 30, 40, 50]
print(f"l3 before :{l3}")

# copy l3 to l4
l4 = l3.copy()          # deep copy - only the data gets copied

print(f"l4 before :{l4}")

l4.extend([60, 70, 80])
print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print("-" * 60)
print("-" * 60)

l5 = [1, 2, 3, [2, 4, 6, 8], 4, 5]
print(f"l5 before :{l5}")

# copy l5 to l6
l6 = l5.copy()          # deep copy

print(f"l6 before :{l6}")

l6[3].extend([10, 12, 14])
print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print("-" * 60)
print("-" * 60)
l7 = [5, 10, 15, 20, [1, 2, 3, 4, 5], 25]
print(f"l7 before :{l7}")

# copy l7 to l8
from copy import deepcopy
l8 = deepcopy(l7)
print(f"l8 before :{l8}")

l8[4].append(6)
l8[4].append(7)
l8[4].append(8)

print(f"l8 after :{l8}")
print(f"l7 after :{l7}")

print("-" * 60)
"""
reverse - changes the original list
reversed - takes a copy of the list and modifies it
"""
l1 = list(range(1, 11))
print(f"l1 :{l1}")

l1.reverse()
print(f"l1 :{l1}")

print("clear".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")
