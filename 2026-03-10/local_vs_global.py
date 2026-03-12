# x = 4

def func() -> None:
    global x
    x = 99
    print(x)

print(f'x = {x}')
func()
print(f'x = {x}')


