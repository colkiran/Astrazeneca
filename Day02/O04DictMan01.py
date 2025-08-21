
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print('-' * 60)
d2 = {'name': 'Sachin', 'age': 32, 'runs': 89, 'oppn': 'Aus'}
print(f"d2 :{d2}")
print(type(d2))

print('-' * 60)
d3 = dict([('name', 'Rahul'), ('age', 31), ('run', 120), ('oppn', 'england')])
print(f"d3 :{d3}")
print(type(d3))

print('-' * 60)
d4 = dict(name="Sourav", age=32, runs=75, oppn='SA')
print(f"d4 :{d4}")
print(type(d4))

print('-' * 60)
# CRUD

# creating
player = {'name': 'Sachin', 'age': 35, 'runs': 135, 'oppn': 'Aus'}
print(f"player :{player}")


print('-' * 60)
# reading
print(f"Name :{player['name']}")
print(f'runs :{player["runs"]}')

print('-' * 60)
for i in player:
    print(i, "=>", player[i])

print('-' * 60)
# update  - a. modify, b. add new value pairs
print(f"player :{player}")
player['name'] = 'Tendulkar'
player['runs'] = 50

player['venue'] = 'Gabba'
player['year'] = 2008

print(f"player :{player}")

print('-' * 60)
# delete
del player['runs']
del player['age']

print(f"player :{player}")

print('-' * 60)
print(dir(player))
