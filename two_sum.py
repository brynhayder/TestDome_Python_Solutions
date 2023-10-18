def find_two_sum_slow(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    for i, x in enumerate(numbers[:-1]):
        for j, y in enumerate(numbers[i+1:]):
            if x + y == target_sum:
                return i, j+i+1
    return None

def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    deltas = dict(
            (y, x) for x, y in enumerate(target_sum - x for x in numbers)
            )
    for i, x in enumerate(numbers):
        # this line works bc of dict insertion priority
        if x in deltas and deltas[x] != i:
            return (i, deltas[x])
    else:
        return None

if __name__ == "__main__":
    numbers_and_targets = [
        ([3, 1, 5, 7, 5, 9], 10) ,
        ([5, 1, 5, 7, 5, 9], 10) ,
        ([5,], 10) ,
        ([5, 1, 5, 7, 5, 9], 8) ,
        ([3, 3], 6),
    ]

    print("-"*5)
    for numbers, target in numbers_and_targets:
        print(numbers)
        # print(numbers[:-1])
        print(target)
        print(find_two_sum(numbers, target))
        print("-"*5)
