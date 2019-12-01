# Count-min sketch

#### Definition:
The **count-min sketch** is a probabilistic data structure that serves as a frequency 
table of events in stream of data. It uses hash functions to map events to frequencies. 
It uses only sub-linear space ate the expense of over-counting some events due to 
collisions.
The Count-min sketch structure is a table of **w** columns, **d** rows and **d**
hash function (one hash function by row).
The structure is initially initialized with null cells.

To **add an element** to the count-min sketch, first you have to hash the item's name.
Then extract it's modulo **w**. This is the item's address. Finally add the item's 
frequency to it's address in the first row. Repeat this process **d** times (using 
**d** different hash functions), once for each row.

To **retrieve an item's frequency**, first compute the **d** hashes modulo **w**
of the item's name. Use these addresses to retrieve the according cells in the 
structure. Finally keep the minimum value from the retrieved ones.

> NB: The count-min sketch tends to **overestimate** the frequency. This is the 
consequence of collisions.

#### Usage:
Install the count-min sketch library. Go to the count_min_sketch folder and run:
```bash
pip install .
```

The class __CountMinSketch__ can be used to create count-min sketch with custom 
number of columns **w** and rows **d**.

```python
from count_min_sketch import CountMinSketch

count_min_sketch = CountMinSketch(nb_columns=w, nb_rows=d)
```
