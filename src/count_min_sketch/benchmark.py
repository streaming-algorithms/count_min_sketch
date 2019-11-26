from random import randint


def absolute_error(expected, actual):
    return abs(expected - actual)


def split_number(number, max_splits):
    splits = list()
    while number > 0 and len(splits) < max_splits - 1:
        split = randint(1, number)
        number -= split
        splits.append(split)
    if max_splits > 0:
        splits.append(number)
    return splits
