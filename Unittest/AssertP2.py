def sum_numbers(n1: int, n2: int) -> int:
    """Sum two numbers

    Args:
        n1 (int): Number 1
        n2 (int): Number 2

    Returns:
        int: Sum of n1 and n2
    """
    return n1 + n2

if __name__ == '__main__':
    res = sum_numbers(10, 20)
    print(res)