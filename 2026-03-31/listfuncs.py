def my_sum(lst: list[int]) -> int:
    """
    Computes the sum of all the elements in list lst.
    Returns zero if the list is empty.
    """
    sum = 0
    for elem in lst:
        sum += elem
    return sum

def my_max(lst: list[int]) -> int | None:
    """
    Finds and returns the largest value
    in a non-empty list of integers.
    If the list is empty, the function
    returns None.
    """
    if len(lst) == 0:
        return None
    largest = lst[0]
    for elem in lst:
        if elem > largest:
            largest = elem
    return largest
    



