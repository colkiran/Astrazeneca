
"""
int
float
complex
"""

a = 100
b = - 100

print(f"a :{a}")    # interpolation
print(type(a))      # RTTI - Run Time Type Identification
print(f"b :{b}")
print(type(b))

print("-" * 60)
c = 100.03
d = -100.2
print(f"c: {c}")
print(type(c))
print(f"d :{d}")
print(type(d))

print("-" * 60)
e = +2e3
f = -2e3
print(f"e :{e}")
print(type(e))
print(f"f :{f}")
print(type(f))

print("-" * 60)
g = 3.14j
h = -3.14j
print(f"g :{g}")
print(type(g))
print(f"h :{h}")
print(type(h))

print("-" * 60)
print(max(33, 56, 89, 20, 15))
print(min(33, 56, 89, 20, 15))

print("-" * 60)
x = 2 + 3.5
print(type(x))

print("-" * 60)
x = 2
y = 3.5
z = x + y
print("x = ", type(x))
print("y = ", type(y))
print("z = ", type(z))

print("conversion".center(60, "-"))
a = 100
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number System".center(60, "-"))
print(f"11 :{11}")          # decimal
print(f"0b11 :{0b11}")      # binary
print(f"0b101 :{0b101}")    # binary
print(f"0o11 :{0o11}")      # octal
print(f"0o101 :{0o101}")    # octal
print(f"0xa :{0xa}")        # hexa
print(f"0xe :{0xe}")        # hexa

print('Number System Conversion'.center(60,  "-"))
a = 100
print(f"binary val of {a} :{bin(a)}")
print(f"Octal of {a} :{oct(a)}")
print(f"hexa of {a} :{hex(a)}")
