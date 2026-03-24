def factorial(n: int) -> int:
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def factorial2(n: int) -> int:
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product

def factorial3(n: int) -> int:
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product



if __name__ == '__main__':
    from time import perf_counter_ns

    for i in range(0, 16):
        print(f'factorial({i:2}) = {factorial(i):13}   factorial2({i:2}) = {factorial2(i):13}')

    
    start = perf_counter_ns()
    for i in range(1000):
        factorial(900)
    stop = perf_counter_ns()
    elapsed = stop - start

    start2 = perf_counter_ns()
    for i in range(1000):
        factorial2(900)
    stop2 = perf_counter_ns()
    elapsed2 = stop2 - start2

    start3 = perf_counter_ns()
    for i in range(1000):
        factorial3(900)
    stop3 = perf_counter_ns()
    elapsed3 = stop3 - start3



    print(f'factorial = {elapsed/1000000000}, factorial2 = {elapsed2/1000000000}, factorial3 = {elapsed3/1000000000}')

