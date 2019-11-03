import numpy as np


class CountMinSketch:
    def __init__(self, nb_columns, nb_rows):
        self.table = [[0 for _ in range(nb_columns)] for _ in range(nb_rows)]
        self.nb_rows = nb_rows
        self.nb_columns = nb_columns

    def add_item(self, item, frequency):
        for row in range(self.nb_rows):
            column = hash(str(row) + item) % self.nb_columns
            self.table[row][column] += frequency

    def retrieve_item_frequency(self, item):
        return np.min(
            [self.table[row][hash(str(row) + item) % self.nb_columns] for row in
             range(self.nb_rows)])

    @classmethod
    def from_error(cls, stream_size, absolute_error, error_probability):
        return cls(nb_columns=int(np.ceil(np.exp(1) * stream_size / absolute_error)),
                   nb_rows=int(np.ceil(np.log2(1 / error_probability))))
