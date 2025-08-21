
def greet():
    print("Greetings Mr.Sachin, Welcome to the event......")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event.")

# city
def greetGstCty(gname,  city="Mumbai"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event.... ")


greet()
print('-' * 60)

greetGst("Sachin")
greetGst('Rohit')

print('-' * 60)
greetGstCty("Sachin")
greetGstCty("Rohit")
greetGstCty("Rahul", "Bangalore")

print('-' * 60)
def admsn(name, dob, qlf, gender, contno, city, addrs):
    print(f"Name :{name}")
    print(f"DOB :{dob}")
    print(f"Qualification :{qlf}")
    print(f"Gender :{gender}")
    print(f"Contact No. :{contno}")
    print(f"City :{city}")
    print(f"Address :{addrs}")

# *args
admsn('John', '16/08/1998', 'Bachelors in Engineering', "Male", "234298374", "Bangalore", "8th main, 5th MG Road")

print("-" * 60)
# **kwargs
admsn(city="Chennai", contno="823798234", gender='Female', addrs = "5th cross, Anna Nagar", name="Grace",  qlf="Bachelors of science", dob="09/05/2000")

print("-" * 60)
# variable length args
def prodAll(*numbers):
    print(numbers)
    print(*numbers)     # unpacking
    prod = 1
    for number in numbers:
        prod *= number
    return prod

res = prodAll(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 60)
def acceptDet(**detials):
    print(detials)
    for k, v in detials.items():
        print(k, "=>", v)


acceptDet(name="Sachin", age=32, runs=120, oppn='SA', venue='Chepauk')

print("-" * 60)
# function can return values

def multiplyMe(x, y):
    return x * y

a = 4
b = 9
print(f"Product {a} and {b} is {multiplyMe(a, b)}")

print("-" * 60)
def arithCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = arithCalc(20, 8)
print(f"res :{res}")

print("-" * 60)
# python supports recursive calls

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

x = -1
print(f"The factorial of {x} is {fact(x)}")

