import pytest
from count_min_sketch.benchmark import absolute_error, split_number


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
