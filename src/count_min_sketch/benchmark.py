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


def generate_data(nb_observations, min_frequency, max_frequency, max_splits=5):
    data = list()
    description = dict()
    for observation in range(nb_observations):
        frequency = randint(min_frequency, max_frequency)
        description[observation] = frequency
        splits = split_number(number=frequency, max_splits=max_splits)
        data.extend([(observation, split) for split in splits])
    return data, description
