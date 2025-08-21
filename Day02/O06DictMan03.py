
print("items".center(60, "-"))
# items - keys + values

emp = {'name': 'Kevin', 'age': 34, 'dept': 'HR', 'desig': 'BDE', 'salary': 65000}
print(f"emp :{emp}")

for k, v in emp.items():
    print(k + " => " + str(v))

print("update".center(60, "-"))
emp1 = {'name': 'Kevin', 'age': 34, 'dept': 'HR', 'desig': 'BDE'}
print(f"emp1 :{emp1}")

print("-" * 60)
emp2 = {'name': 'Kenith', 'age': 30, 'dept': 'Finance', 'salary': 65000}
print(f"emp2 :{emp2}")

print("-" * 60)
# update the values of emp1 with emp2
emp1.update(emp2)
print(f"emp1 :{emp1}")