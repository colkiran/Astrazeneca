
def fun(x):
    print(f"inside function before :{x}")
    x += 100
    print(f"inside function after :{x}")

a = 50

print(f"before the function call :{a}")

fun(a)

print(f"after the function call :{a}")
