
Matrix = list[list[int]]

def print_matrix1(a: Matrix) -> None:
    for row in range(len(a)):
        for column in range(len(a[row])):
            print(f'{a[row][column]:4}', end='')
        print()

def print_matrix2(a: Matrix) -> None:
    for row in a:
        for elem in row:
            print(f'{elem:4}', end='')
        print()


if __name__ == '__main__':
    m1 = [[1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]]

    m2 = [[10, 20, 30, 40, 50], 
        [60, 70, 80, 90, 100], 
        [110, 120, 130, 140, 150]]

    print_matrix1(m1)
    print('----------------')
    print_matrix1(m2)
    print('======================================')

    print_matrix2(m1)
    print('----------------')
    print_matrix2(m2)
