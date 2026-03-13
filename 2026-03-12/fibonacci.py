def fib(k: int) -> int:
    if k == 0:
        return 0
    elif k == 1:
        return 1
    else:
        return fib(k - 2) + fib(k - 1)


for i in range(0, 13):
    print(f'{i:2}: {fib(i): 3}')