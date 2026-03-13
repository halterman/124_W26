def factorial2(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial2(n - 1)
    
for i in range(0, 21):
    print(f'factorial2({i:20}) = {factorial2(i):20}')

print(factorial2(-1))