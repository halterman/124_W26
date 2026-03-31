from listfuncs import my_sum, my_max  # type: ignore


def test_my_sum() -> None:
    """
    >>> my_sum([10, 20, 30, 40, 50])
    150
    >>> my_sum([15])
    15
    >>> my_sum([])
    0
    """

def test_my_max() -> None:
    """
    >>> my_max([10, 20, 80, 30, 40, 50])
    80
    >>> my_max([15])
    15
    >>> my_max([])
    >>> my_max([80, 20, 30])
    80
    >>> my_max([20, 30, 80])
    80
    """
