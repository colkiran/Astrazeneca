
for i in range(1, 11):
   print(i, end=" ")
print()

print("-" * 60)

for i in range(1, 21):
    # if i > 12:
    #     break               # stop the iteration
    if i % 2 == 0:
        continue            # skip the current iteration
    print(i, end=" ")
else:
    print("\n completed generating numbers.....")