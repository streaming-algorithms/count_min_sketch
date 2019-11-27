from collections import defaultdict

import pytest
from count_min_sketch.benchmark import absolute_error, generate_data, split_number


@pytest.mark.parametrize('expected, actual', [
    (100, 101),
    (101, 100),
    (0, 36),
    (10000, 1)
])
def test_absolute_error(expected, actual):
    assert absolute_error(expected=expected, actual=actual) == abs(expected - actual)


@pytest.mark.parametrize('number, max_splits', [
    (100, 10),
    (50, 3),
    (10, 10),
    (42, 31)
])
def test_split_number(number, max_splits):
    splits = split_number(number=number, max_splits=max_splits)
    assert len(splits) <= max_splits
    assert sum(splits) == number
    assert 0 not in splits


@pytest.mark.parametrize('nb_observations, min_frequency, max_frequency, max_splits', [
    (4, 1, 10, 3),
    (100, 100, 200, 10),
    (1, 1, 1, 1)
])
def test_generate_data(nb_observations, min_frequency, max_frequency, max_splits):
    data, description = generate_data(
        nb_observations=nb_observations,
        min_frequency=min_frequency,
        max_frequency=max_frequency,
        max_splits=max_splits
    )
    # test description
    assert len(description.items()) == nb_observations
    for observation, frequency in description.items():
        assert -1 < observation < nb_observations
        assert min_frequency <= frequency <= max_frequency
    # test data
    data_desc = defaultdict(lambda: {'frequency': 0, 'splits': 0})
    for observation, frequency in data:
        data_desc[observation]['frequency'] += frequency
        data_desc[observation]['splits'] += 1
    assert len(data_desc.items()) == nb_observations
    for observation, desc in data_desc.items():
        assert -1 < observation < nb_observations
        assert min_frequency <= desc['frequency'] <= max_frequency
        assert desc['splits'] <= max_splits
