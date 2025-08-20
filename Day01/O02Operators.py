"""
Arithmetic
Augmentor : =, +=, -=, *=
comparison or relational : ==, >, <, >=, <=, !=
logical - and, or, not
bitwise
ternary
"""
print("Arithmetic Operator".center(60,"-"))
print(f"sum 10 + 3 = {10 + 3}")
print(f"diff 10 - 3 = {10 - 3}")
print(f"prod 10 * 3 = { 10 * 3}")
print(f"Quot 10 / 3 = {10 / 3}")
print(f"floor 10 // 3 = {10 // 3}")
print(f"Mod 10 % 3 = {10 % 3}")
print(f"power  10 ** 3 = {10 ** 3}")

print("Augmentor".center(60, "-"))
#  =, += , -=, *=
x = 5
print(f"x :{x}")

x *= 3
print(f"x :{x}")

x /= 5
print(f"x :{x}")

print("comparison operators".center(60, "-"))
#  ==, >, >=, <, <=, !=
a = 1
b = 2
print(f"a = {a}, b = {b}")
print(f"a == b :{a == b}")
print(f"a >= b :{a >= b}")
print(f"a <= b :{a <= b}")
print(f"a != b :{a != b}")

print("logical operators".center(60, "-"))
# and, or , not
print(f"1 == 1 and 2 == 2 :{1 == 1 and 2 == 2}")
print(f"1 == 1 and 1 == 2 :{1 == 1 and 1 == 2}")

print(f"1 == 1 or 2 == 2 :{1 == 1 or 2 == 2}")
print(f"1 == 2 or 1 == 2 :{1 == 1 or 1 == 2}")

print(f"not(1 == 2 or 1 == 2) :{not(1 == 1 or 1 == 2)}")
print(f"not(1 == 1 and 2 == 2) :{not(1 == 1 and 2 == 2)}")

print('-' * 60)
print(f"ord('a') :{ord('a')}")   # integer representation of unicode characters
print(f"ord('z') :{ord('z')}")
print(f"ord('A') :{ord('A')}")
print(f"ord('Z') :{ord('Z')}")

print('-' * 60)
print(f"chr(65) :{chr(65)}")
print(f"chr(90) :{chr(90)}")
print(f"chr(97) :{chr(97)}")
print(f"chr(122) :{chr(122)}")

print("ternary operator".center(60, "-"))
age = 19
print("Eligible" if age > 17 else "Not Eligible")

print("Bitwise Operator".center(60, "-"))
print(f"5 | 3 :{5 | 3}")
print(f"5 & 3 :{5 & 3}")
print(f"5 ^ 3 :{5 ^ 3}")
print(f"5 << 1 :{5 << 1}")
print(f"8 << 1 :{8 << 1}")
print(f"5 << 2 :{5 << 2}")
print(f"16 >> 1 :{16 >> 1}")
print(f"5 >> 1 :{5 >> 1}")