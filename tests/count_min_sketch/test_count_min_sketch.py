import pytest

from count_min_sketch.count_min_sketch import CountMinSketch


class TestCountMinSketch:
    @pytest.mark.parametrize("nb_columns, nb_rows", [
        (1000, 10),
        (100, 4),
        (10, 8)
    ])
    def test_table(self, nb_columns, nb_rows):
        count_min_sketch = CountMinSketch(nb_columns=nb_columns, nb_rows=nb_rows)
        assert count_min_sketch.table == [[0 for _ in range(nb_columns)] for _ in
                                          range(nb_rows)]
        assert count_min_sketch.nb_rows == nb_rows
        assert count_min_sketch.nb_columns == nb_columns

    @pytest.mark.parametrize("item, frequency", [
        ("bloom", 10),
        ("filter", 1000),
        ("data", 32)
    ])
    def test_add_item(self, item, frequency):
        nb_columns = 1000
        nb_rows = 10
        count_min_sketch = CountMinSketch(nb_columns=nb_columns, nb_rows=nb_rows)
        old_values = [[row, hash(str(row) + item) % nb_columns,
                       count_min_sketch.table[row][hash(str(row) + item) % nb_columns]]
                      for row in range(nb_rows)]
        count_min_sketch.add_item(item=item, frequency=frequency)
        for row, column, old_value in old_values:
            assert count_min_sketch.table[row][column] == old_value + frequency

    @pytest.mark.parametrize("item, table, expected", [
        ("bloom", [[row + 10 for _ in range(100)] for row in range(10)], 10),
        ("filter", [[row + 42 for _ in range(100)] for row in range(10)], 42),
        ("data", [[row for _ in range(100)] for row in range(10)], 0)
    ])
    def test_retrieve_item_frequency(self, item, table, expected):
        nb_columns, nb_rows = len(table[0]), len(table)
        count_min_sketch = CountMinSketch(nb_columns=nb_columns, nb_rows=nb_rows)
        count_min_sketch.table = table
        assert count_min_sketch.retrieve_item_frequency(item=item) == expected
