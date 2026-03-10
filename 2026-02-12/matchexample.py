x = int(input())
y = int(input())
print(x/y)


number = input("Please enter the English number: ")
match number:
    case 'one':
        spanish_word = 'uno'
    case 'two':
        spanish_word = 'dos'
    case 'three':
        spanish_word = 'tres'
    case 'four':
        spanish_word = 'cuatro'
    case _:
        spanish_word = "???"
print(f'The Spanish equivalent is {spanish_word}')