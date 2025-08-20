
st = "2397423astrazeneca894382364"
# extract the name from the above string
l=len(st)
for i in range(0,l):
    if st[i].isalpha():
        print(st[i], end="")
print()
print('-' * 60)
# maketrans, translate, format
st = "hello world"
print(f"st :{st}")
# length of a and b should be the same
a = 'helowrd'
b = 'HELOWRD'
res = st.maketrans(a, b)
print(f"res :{res}")

res1 = st.translate(res)
print(f"res1 :{res1}")

print("-" * 60)
# format
print("Welcome {}, what a {} player".format("Sachin", "superb"))
print("Welcome {name}, what a {adj} player".format(name = "Sachin", adj =  "superb"))
print("Welcome {name} with a rating of {rat:.2f}, what a {adj} player for {ctry}".format(name="Sachin", rat=4.872357332, adj = "class", ctry="India"))

print("-" * 60)
print("{val} {val} {val}".format(val = 'A'))
print("{val!s} {val!r} {val!a}".format(val = 'A'))

print("{num} {num} {num}".format(num=36))
print("{num:10} {num:b} {num:f}".format(num=36))
print("{num:5} {num:b} {num:f}".format(num=36))
print("{num:5} {num:b} {num:f}".format(num=363445756567))

# alignment
print("{num:15}Tendulkar".format(num="Sachin"))
print("{num:15}Tendulkar".format(num=387))
print("{num:>15} Tendulkar".format(num="Sachin"))           # right
print("{num:^15} Tendulkar".format(num="Sachin"))           # center
print("{num:<15} Tendulkar".format(num="Sachin"))           # left

print("{num:10} Tendulkar".format(num=5000))
print("{num:010} Tendulkar".format(num=5000))
print("{num:-^60}".format(num="hello"))
print("hello".center(60, "-"))

print("{num:.6}".format(num="Sachin Tendulkar"))
from math import pi
print("{num}".format(num = pi))
print("{num:010.2}".format(num = pi))
print("{num:010.3}".format(num = pi))
print("{num:010.4}".format(num = pi))
print("{num:010.5}".format(num = pi))
