def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


for i in range(3):
    print(fib(i))
