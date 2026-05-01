def select_sort(a: list[int]) -> None:
    n = len(a)
    i = 0
    while i < n - 1:
        j = i + 1
        smallest = i
        while j < n:
            if a[j] < a[smallest]:
                smallest = j
            j += 1
        if smallest != i:
            a[i], a[smallest] = a[smallest], a[i]
        i += 1

def select_sort2(a: list[int]) -> None:
    n = len(a)
    for i in range(0, n - 1):
        smallest = i
        for j in range(i + 1, n):
            if a[j] < a[smallest]:
                smallest = j
        if smallest != i:
            a[i], a[smallest] = a[smallest], a[i]


lst = [5, -67, 3, 0, 7, 12, 21, 3]
print(f'Before: {lst}')
select_sort2(lst)
print(f'After:  {lst}')
