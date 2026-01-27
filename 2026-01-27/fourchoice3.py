def fourchoice(option: str) -> None:
    if option == 'A':
        print('You chose symbol "A"')
    elif option == 'B':
        print('You chose symbol "B"')
    elif option == 'C':
        print('You chose symbol "C"')
    else:
        print('You chose neither "A nor B nor C"')


choice = input('Please enter A, B, or C: ')
fourchoice(choice)
