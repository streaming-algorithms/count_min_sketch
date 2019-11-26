import pytest

from count_min_sketch.benchmark import absolute_error


@pytest.mark.parametrize('expected, actual', [
    (100, 101),
    (101, 100),
    (0, 36),
    (10000, 1)
])
def test_absolute_error(expected, actual):
    assert absolute_error(
        expected=expected,
        actual=actual
    ) == abs(expected - actual)
