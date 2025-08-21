
print('keys'.center(60,"-"))
d1 = {'name': 'Kevin', 'age': 34, 'dept': 'HR', 'desig': 'BDE', 'salary': 65000}
print(f"d1 :{d1}")

k = d1.keys()
print(f"k :{k}")

print("-" * 60)
for k in d1.keys():
    print(k, "=>", d1[k])

print("values".center(60, "-"))
print(f"d1 :{d1}")

print("-" * 60)
v = d1.values()
print(f"v :{v}")

print("get".center(60, "-"))
print(f"d1 :{d1}")

print(f"Name :{d1.get('name', 'Invalid key,  please enter a valid key')}")
print(f"desig :{d1.get('desg', 'Invalid key,  please enter a valid key')}")


print("setdefault".center(60,"-"))
# only add new key value pairs into the dictionary, does not allow to modify the existing keys and values

player = {'name': 'Kevin', 'age': 34, 'dept': 'HR', 'desig': 'BDE', 'salary': 65000}
print(f"player :{player}")

print("-" * 60)
player.setdefault('name', 'Costner')
player.setdefault('dept', 'Finance')

player.setdefault('loc', 'Chennai')
player.setdefault('gender', 'male')

print(f"player :{player}")

print("fromkeys".center(60, "-"))
# convert a list into a dictionary

cities = ['blr', 'che', 'mum', 'del', 'hyd', 'kol']
print(f"cities :{cities}")

res1 = dict.fromkeys(cities)
print(f"res1 :{res1}")

res2 = dict.fromkeys(cities, 24)
print(f"res2 :{res2}")

print("pop".center(60, "-"))

emp = {'name': 'Kevin', 'age': 34, 'dept': 'HR', 'desig': 'BDE', 'salary': 65000}
print(f"emp :{emp}")

res = emp.pop('desig')
print(f"res :{res}")

res = emp.pop('age')
print(f"res :{res}")

# res = emp.pop('loc')
# print(f"res :{res}")

print(f"emp :{emp}")

print("popitem".center(60, "-"))

emp = {'name': 'Kevin', 'age': 34, 'dept': 'HR', 'desig': 'BDE', 'salary': 65000}
print(f"emp :{emp}")

res = emp.popitem()
print(f"res :{res}")

res = emp.popitem()
print(f"res :{res}")

print(f"emp :{emp}")