
def fun(empnames):
    print(f"inside the function before :{empnames}")
    empnames.extend(['ruben', 'john', 'charles'])
    print(f"inside the function after :{empnames}")

enames = ['richard', 'pinto', 'ruben', 'peter']

print(f'before the function call :{enames}')

fun(enames)

print(f'after the function call :{enames}')
