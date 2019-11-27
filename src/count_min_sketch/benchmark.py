from random import randint

from count_min_sketch.count_min_sketch import CountMinSketch


def absolute_error(expected, actual):
    return abs(expected - actual)


def split_number(number, max_splits):
    splits = list()
    while number > 0 and len(splits) < max_splits - 1:
        split = randint(1, number)
        number -= split
        splits.append(split)
    if number > 0:
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


def benchmark(nb_columns, nb_rows, data, description):
    count_min_sketch = CountMinSketch(nb_columns=nb_columns, nb_rows=nb_rows)
    for item, frequency in data:
        count_min_sketch.add_item(item=item, frequency=frequency)
    abs_error = list()
    nb_errors = 0
    for item, expected_frequency in description.items():
        actual_frequency = count_min_sketch.retrieve_item_frequency(item=item)
        nb_errors += actual_frequency != expected_frequency
        abs_error.append(
            absolute_error(
                expected=expected_frequency,
                actual=actual_frequency
            )
        )
        nb_items = len(description.items())
    return sum(abs_error) / nb_items, nb_errors / nb_items
