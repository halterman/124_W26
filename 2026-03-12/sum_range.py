def sum_range(n: int=10, m: int=100) -> int:
    sum = 0
    for val in range(n, m + 1):
        sum += val
    return sum
