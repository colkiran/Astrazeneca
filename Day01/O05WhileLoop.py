
x = 1
while x < 11:
    print(x, end=" ")
    x += 1
print()

print("-" * 60)
print(f'after :{x}')
while True:
    print(x, end=" ")
    x -= 1
    if x == 0:
        break