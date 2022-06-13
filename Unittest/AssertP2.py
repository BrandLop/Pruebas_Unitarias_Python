def sum_numbers(n1: int, n2: int) -> int:
    """Sum two numbers positives

    Args:
        n1 (int): Number 1
        n2 (int): Number 2

    Returns:
        int: Sum of n1 and n2
    """
    assert n1 > 0 and n2 > 0, "Both numbers must be positive"
    return n1 + n2

if __name__ == '__main__':
    res = sum_numbers(-10, 20)
    print(res)